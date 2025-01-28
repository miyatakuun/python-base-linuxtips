<h2>⚙️ Como executar o sistema:</h2>

<ol>
  <li>Para rodar o sistema:
    <pre><code>
docker-compose rm
docker-compose build
docker-compose up
    </code></pre>
  </li>
  <li>
    <strong>Modo desenvolvedor</strong> (usando o banco do container e Flask no VSCode):
    <ol>
      <li>Inicie o sistema (passo 1).</li>
      <li>Pare o container do Flask:
        <pre><code>
docker ps
docker stop &lt;CONTAINER_ID_DO_FLASK&gt;
        </code></pre>
      </li>
      <li>Execute o Flask diretamente:
        <pre><code>
export FLASK_APP=app_factory.py
flask run
        </code></pre>
      </li>
    </ol>
  </li>
</ol>

<p><strong>Dica:</strong> Use <code>docker ps</code> para listar os containers ativos e encontrar o ID do container do Flask.</p>
