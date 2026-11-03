---
content_hash: 5bf7be650dd84ccbcd6a8b802a780617443fbf0773b9917eaebc96d9e76d36e8
fetched_at: '2026-06-29T00:11:04.250364+00:00'
page_id: '625762715'
product: rm
source: tdn-rm
title: FAQ - Novos portais
type: documentation
url: https://tdn.totvs.com/display/LRM/FAQ+-+Novos+portais
version: 22
---

Bem-vindo ao canal de ajuda! Aqui você encontra as respostas para as dúvidas mais comuns sobre o **Portal de Gestão Educacional**, o **Portal da Biblioteca** e o **Novo Portal do Professor**.

Após configurar o portal do professor e acessar a URL, ocorre o erro: Servidor não está respondendo.

**Problema:** Erro "Servidor não está respondendo" ao acessar a URL do Portal do Professor após a configuração.

**Solução:** Verifique se o módulo **Application Request Routing Cache (ARR)** está habilitado no IIS. 👉 [Clique aqui para acessar o item da documentação](https://tdn.totvs.com/x/9Cd0Ig).

Após configurar o portal do professor é realizado o login porém não é redirecionado para a página principal.

**Solução:** Verifique a ordenação das regras de *URL Rewrite* do Portal do Professor. A regra correspondente ao **"AliasName"** deve, obrigatoriamente, ficar posicionada antes (anteceder) da regra da **"Api"**.

Erro ao tentar fazer o upload de arquivos maiores que 30 MB**Erro no upload de arquivos acima de 30 MB (Materiais):** > O limite máximo de requisição do servidor foi atingido. Para o passo a passo completo, [consulte a documentação técnica aqui](https://tdn.totvs.com/display/LRM/Configurar+upload+de+arquivos+grandes).Divergências entre Ambientes (Produção x Troubleshooting)

**Problema:** O ambiente apresenta comportamentos diferentes ou não carrega as últimas atualizações devido a arquivos de cache (*chunks*) desatualizados no arquivo principal de inicialização.

#### **Solução:**

1. **Localize o arquivo de configuração:** Acesse o servidor e encontre o arquivo `index.html` dentro da pasta correspondente ao portal analisado.

   > 📁 **Exemplo de diretório:**
   >
   > `...\FrameHTML\web\app\Edu\portalgestaoeducacional`
2. **Verifique os pacotes de atualização (*chunks*):**

   * Abra o arquivo `index.html` em um editor de texto e observe o conteúdo das tags `<link>` e `<script>`.

* + Confirme se os arquivos de "chunk" (ex: `main.xxxxxx.js` ou `styles.xxxxxx.css`) referenciados no código são os mesmos que estão fisicamente na pasta.
  + **💡 Dica prática:** Organize os arquivos da pasta por **Data de Modificação** (do mais recente para o mais antigo) e compare os nomes dos arquivos mais novos com as linhas escritas dentro do `index.html`.

**Acione o suporte técnico (Se houver divergência):** Se você constatar que os pacotes referenciados no `index.html` estão desatualizados ou apontando para arquivos inexistentes, será necessária uma reinstalação:

* + Abra um chamado para a equipe de **Suporte Cloud**.
  + Solicite uma **nova implantação/instalação dos portais**.
  + **Justificativa do chamado:** Informar que há divergência de pacotes no `index.html` e o objetivo é atualizar os *chunks* para que o sistema inicialize com as modificações mais recentes.
