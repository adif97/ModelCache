# -*- coding: utf-8 -*-
import asyncio

from modelcache.utils.error import RemoveError


async def adapt_remove(*args, **kwargs):
    chat_cache = kwargs.pop("cache_obj")
    model = kwargs.pop("model", None)
    remove_type = kwargs.pop("remove_type", None)
    require_object_store = kwargs.pop("require_object_store", False)
    if require_object_store:
        assert chat_cache.data_manager.o, "Object store is required for adapter."

    # delete data
    if remove_type == 'delete_by_id':
        id_list = kwargs.pop("id_list", [])
        resp = await asyncio.to_thread(
            chat_cache.data_manager.delete,
            id_list, model=model
        )
    elif remove_type == 'truncate_by_model':
        resp = await asyncio.to_thread(
            chat_cache.data_manager.truncate,
            model
        )
    else:
        # resp = "remove_type_error"
        raise RemoveError()
    return resp

