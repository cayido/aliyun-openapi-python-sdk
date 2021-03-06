# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class PutBucketLimitRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OssAdmin', '2013-07-12', 'PutBucketLimit','ossadmin')

	def get_uid(self):
		return self.get_query_params().get('uid')

	def set_uid(self,uid):
		self.add_query_param('uid',uid)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_bid(self):
		return self.get_query_params().get('bid')

	def set_bid(self,bid):
		self.add_query_param('bid',bid)

	def get_BucketLimit(self):
		return self.get_query_params().get('BucketLimit')

	def set_BucketLimit(self,BucketLimit):
		self.add_query_param('BucketLimit',BucketLimit)