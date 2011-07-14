#!/bin/bash
curl -G -H "Content-Type: text/xml" -d "cluster_id=1;node_id=2;latest=20" http://localhost:8000/api/v1/xml/clusters
