<h1>Hardening Docker Containers with Security Best Practices</h1>


<h2>Description</h2>
 This project demonstrates how to secure Docker containers using best practices.  It includes running containers as non-root users, enabling Docker Content Trust, signing and verifying images, scanning images for vulnerabilities, dropping unnecessary privileges, and running containers with read-only file systems. Together, these practices ensure container integrity, reduce attack surfaces, and enforce trust in containerized deployments. <br />


<h2>Tools and Technologies</h2>

 <ul>
    <li>Docker</li>
    <li>Docker Compose</li>
    <li>Docker Content Trust (for signing images)</li>
    <li>Docker Scout (security scanning)</li>
    <li>Flask </li>
    <li>Ubuntu 24.04 LTS</li>
  </ul>

<h2>Project Walk-through</h2>

<p align="center">
1. Create a simple Flask web application and Dockerfile that runs as a non-root user <br />
<img src="https://i.postimg.cc/02GPFwvB/1.jpg"/>
<br />
<br />
2. Enable Docker Content Trust, generate signing keys, and sign your Docker image <br/>
<img src="https://i.postimg.cc/R0wr8Wj0/2.jpg" />
<br />
<br />
3. Scan the signed image for vulnerabilities using Docker Scout and review the results <br/>
<img src="https://i.postimg.cc/5tVKXnRx/3.jpg"/>
<br />
<br />
4. Harden the container by dropping unnecessary Linux capabilities and using security options. <br/>
<img src="https://i.postimg.cc/wjTcZZZR/4.jpg" />
<br />
<br />
5. Run the container with a read-only file system, allowing writes only where needed <br/>
<img src="https://i.postimg.cc/rmJwBnvz/5.jpg" />
<br />
<br />
6. Deploy the secured container using Docker Compose with all security layers enabled <br/>
<img src="https://i.postimg.cc/HxBTZJyy/6.jpg" />
<br />
<br />
</p>

