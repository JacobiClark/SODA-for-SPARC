from flask_restx import Resource, fields, reqparse
from namespaces import NamespaceEnum, get_namespace

from curate import (
    create_folder_level_manifest,
    check_empty_files_folders,
    main_curate_function,
    main_curate_function_progress,
    generate_manifest_file_locally,
    check_JSON_size,
    main_curate_function_upload_details,
    create_high_level_manifest_files_existing_local_starting_point,
)
from errorHandlers.notBadRequestException import notBadRequestException

api = get_namespace(NamespaceEnum.CURATE_DATASETS)

model_check_empty_files_folders_response = api.model( "CheckEmptyFilesFoldersResponse", {
    "empty_files": fields.List(fields.String),
    "empty_folders": fields.List(fields.String),
    "soda_json_structure": fields.String(description="JSON structure of the SODA dataset"),
})

@api.route("/empty_files_and_folders")
class CheckEmptyFilesFolders(Resource):
    # response types/codes
    @api.doc(responses={500: 'There was an internal server error', 400: 'Bad Request'}, description="Given a sodajsonobject return a list of empty files and folders should they exist, as well as the sodajsonobject.")
    def get(self):

        # get the soda_json_structure from the request object
        args = reqparse.RequestParser()
        args.add_argument("soda_json_structure", type=dict, required=True, help="SODA's Dataset structure", location="json")

        # get the dataset_structure from the request object
        soda_json_structure = args.parse_args().get("soda_json_structure")

        try:
            return check_empty_files_folders(soda_json_structure)
        except Exception as e:
            api.abort(500, str(e))





model_main_curation_function_response = api.model( "MainCurationFunctionResponse", {
    "main_curate_progress_message": fields.String(description="Progress message from the main curation function"),
    "main_total_generate_dataset_size": fields.String(description="Total size of the dataset"),
    "main_curation_uploaded_files": fields.Integer(description="Number of files that are being generated. ")
})

@api.route("/curation")
class Curation(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("soda_json_object", type=dict, required=True, help="SODA's Dataset structure", location="json")

    @api.doc(responses={500: 'There was an internal server error', 400: 'Bad Request', 403: 'Forbidden'}, description="Given a sodajsonobject generate a dataset. Used in the final step of Organize Datasets.")
    @api.marshal_with(model_main_curation_function_response)
    @api.expect(parser)
    def post(self):
        # get the soda_json_structure from the request object
        soda_json_object = self.parser.parse_args().get("soda_json_object")

        try:
            return main_curate_function(soda_json_object)
        except Exception as e:
            if notBadRequestException(e):
                api.abort(500, str(e))
            raise e