#!/bin/bash
curl -G -H "Content-Type: text/xml" -d "cluster_id=2;node_id=4;latest=10" http://localhost:8000/api/v1/xml/clusters
