#!/bin/bash
curl -G -H "Content-Type: text/xml" -d "cluster_id=1;node_id=4;latest=10" http://localhost:8000/api/xml/clusters
