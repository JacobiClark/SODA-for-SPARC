import copy

error_path_report = {
  "#/": {
    "error_count": 1,
    "messages": ["'path_metadata' is a required property"]
  },
  "#/contributors": {
    "error_count": 1,
    "messages": [
      "[{'contributor_name': 'Marroquin, Christopher', 'contributor_orcid': 'https://orcid.org/0000-0002-3399-1731', 'contributor_affiliation': 'https://ror.org/0168r3w48', 'contributor_role': ['PrincipalInvestigator'], 'first_name': 'Christopher', 'last_name': 'Marroquin', 'id': 'https://orcid.org/0000-0002-3399-1731'}] is not valid under any of the given schemas"
    ]
  },
  "#/id": {
    "error_count": 1,
    "messages": [
      "'cgeNh_H8zjDDsGcJn2wlicHHZcjoavLjuiZxzsRAw2ix6Tp4Bwutpuj2ykK8i1JamSX9nurlL6MSLF7LlUicLA:C:/Users/CMarroquin/temp-datasets/DatasetTemplate' does not match '^N:dataset:'"
    ]
  },
  "#/inputs/dataset_description_file": {
    "error_count": 8,
    "messages": [
      "'description' is a required property",
      "'funding' is a required property",
      "'name' is a required property",
      "'protocol_url_or_doi' is a required property"
    ]
  },
  "#/inputs/dataset_description_file/contributors": {
    "error_count": 1,
    "messages": [
      "[{'contributor_name': 'Marroquin, Christopher', 'contributor_orcid': 'https://orcid.org/0000-0002-3399-1731', 'contributor_affiliation': 'https://ror.org/0168r3w48', 'contributor_role': ['PrincipalInvestigator']}] is not valid under any of the given schemas"
    ]
  },
  "#/inputs/manifest_file/-1/contents/manifest_records/-1": {
    "error_count": 1,
    "messages": [
      "{'description': 'j'} is not valid under any of the given schemas"
    ]
  },
  "#/inputs/manifest_file/-1/uri_api": {
    "error_count": 1,
    "messages": [
      "'file://C:/Users/CMarroquin/temp-datasets/DatasetTemplate/manifest.xlsx' does not match '^(https?):\\\\/\\\\/([^\\\\s\\\\/]+)\\\\/([^\\\\s]*)'"
    ]
  },
  "#/inputs/manifest_file/-1/uri_human": {
    "error_count": 1,
    "messages": [
      "'file://C:/Users/CMarroquin/temp-datasets/DatasetTemplate/manifest.xlsx' does not match '^(https?):\\\\/\\\\/([^\\\\s\\\\/]+)\\\\/([^\\\\s]*)'"
    ]
  },
  "#/meta": {
    "error_count": 6,
    "messages": [
      "'award_number' is a required property",
      "'description' is a required property",
      "'funding' is a required property",
      "'modality' is a required property",
      "'organ' is a required property",
      "'title' is a required property"
    ]
  },
  "#/meta/techniques": {
    "error_count": 1,
    "messages": ["[] is too short"]
  },
  "#/meta/timestamp_created": {
    "error_count": 1,
    "messages": ["None is not of type 'string'"]
  },
  "#/meta/uri_api": {
    "error_count": 1,
    "messages": [
      "'file://C:/Users/CMarroquin/temp-datasets/DatasetTemplate' does not match '^https://api\\\\.pennsieve\\\\.io/(datasets|packages)/'"
    ]
  },
  "#/meta/uri_human": {
    "error_count": 1,
    "messages": [
      "'file://C:/Users/CMarroquin/temp-datasets/DatasetTemplate' does not match '^https://app\\\\.pennsieve\\\\.io/N:organization:'"
    ]
  },
  "#/specimen_dirs": {
    "error_count": 3,
    "messages": [
      "'records' is a required property",
      "No folder for sample sam-1",
      "There are specimens that have no corresponding directory!\n{'sub-1_sam-1', 'sub-1'}"
    ]
  }
}




# return the errors from the error_path_report that should be shown to the user.
# as per Tom (developer of the Validator) for any paths (the keys in the Path_Error_Report object)
# with common prefixes, only return the one that doesn't have any errors in its subpaths. 
# e.g., If given #/meta and #/meta/technique keys only return #/meta/technique (as this group doesn't have any subpaths)
def get_target_errors(error_path_report):

  user_errors = copy.deepcopy(error_path_report)

  keys = error_path_report.keys()

  # go through all paths and store the paths with the longest subpaths for each base 
  # also store matching subpath lengths together
  for k in keys:
    prefix = get_path_prefix(k)

    # check for a suffix indicator in the prefix (aka a forward slash at the end of the prefix)
    if prefix[-1] == "/":
      # if so remove the suffix and check if the resulting prefix is an existing path key
      # indicating it can be removed from the errors_for_users dictionary as the current path
      # will be an error in its subpath -- as stated in the function comment we avoid these errors 
      prefix_no_suffix_indicator = prefix[0: len(prefix) - 1]

      if prefix_no_suffix_indicator in user_errors:
        del user_errors[prefix_no_suffix_indicator]


  
  return user_errors
  

def get_path_prefix(path):
  # check if path has one "/"
  if path.count('/') == 1:
    # get the entire path as the "prefix" and return it
    return path 
  else : 
    # get the path up to the final "/" and return it as the prefix
    final_slash_idx = path.rfind("/")
    return path[0: final_slash_idx + 1]
    

    

print(get_target_errors(error_path_report))   


{
    '#/': {
        'error_count': 1,
        'messages': ["'path_metadata' is a required property"]
    },
    '#/contributors': {
        'error_count': 1,
        'messages': ["[{'contributor_name': 'Marroquin, Christopher', 'contributor_orcid': 'https://orcid.org/0000-0002-3399-1731', 'contributor_affiliation': 'https://ror.org/0168r3w48', 'contributor_role': ['PrincipalInvestigator'], 'first_name': 'Christopher', 'last_name': 'Marroquin', 'id': 'https://orcid.org/0000-0002-3399-1731'}] is not valid under any of the given schemas"]
    },
    '#/id': {
        'error_count': 1,
        'messages': ["'cgeNh_H8zjDDsGcJn2wlicHHZcjoavLjuiZxzsRAw2ix6Tp4Bwutpuj2ykK8i1JamSX9nurlL6MSLF7LlUicLA:C:/Users/CMarroquin/temp-datasets/DatasetTemplate' does not match '^N:dataset:'"]
    },
    '#/inputs/dataset_description_file/contributors': {
        'error_count': 1,
        'messages': ["[{'contributor_name': 'Marroquin, Christopher', 'contributor_orcid': 'https://orcid.org/0000-0002-3399-1731', 'contributor_affiliation': 'https://ror.org/0168r3w48', 'contributor_role': ['PrincipalInvestigator']}] is not valid under any of the given schemas"]
    },
    '#/inputs/manifest_file/-1/contents/manifest_records/-1': {
        'error_count': 1,
        'messages': ["{'description': 'j'} is not valid under any of the given schemas"]
    },
    '#/inputs/manifest_file/-1/uri_api': {
        'error_count': 1,
        'messages': ["'file://C:/Users/CMarroquin/temp-datasets/DatasetTemplate/manifest.xlsx' does not match '^(https?):\\\\/\\\\/([^\\\\s\\\\/]+)\\\\/([^\\\\s]*)'"]
    },
    '#/inputs/manifest_file/-1/uri_human': {
        'error_count': 1,
        'messages': ["'file://C:/Users/CMarroquin/temp-datasets/DatasetTemplate/manifest.xlsx' does not match '^(https?):\\\\/\\\\/([^\\\\s\\\\/]+)\\\\/([^\\\\s]*)'"]
    },
    '#/meta/techniques': {
        'error_count': 1,
        'messages': ['[] is too short']
    },
    '#/meta/timestamp_created': {
        'error_count': 1,
        'messages': ["None is not of type 'string'"]
    },
    '#/meta/uri_api': {
        'error_count': 1,
        'messages': ["'file://C:/Users/CMarroquin/temp-datasets/DatasetTemplate' does not match '^https://api\\\\.pennsieve\\\\.io/(datasets|packages)/'"]
    },
    '#/meta/uri_human': {
        'error_count': 1,
        'messages': ["'file://C:/Users/CMarroquin/temp-datasets/DatasetTemplate' does not match '^https://app\\\\.pennsieve\\\\.io/N:organization:'"]
    },
    '#/specimen_dirs': {
        'error_count': 3,
        'messages': ["'records' is a required property", 'No folder for sample sam-1', "There are specimens that have no corresponding directory!\n{'sub-1_sam-1', 'sub-1'}"]
    }
}