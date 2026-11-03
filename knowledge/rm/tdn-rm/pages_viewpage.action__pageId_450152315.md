---
content_hash: 45af7359f3c0880a3ddf4f1e17a80ece98a9b1193589b79dc3ae7e030362e877
fetched_at: '2026-06-29T00:09:55.796572+00:00'
page_id: '450152315'
product: rm
source: tdn-rm
title: 13 - Upload de Arquivos/Documentos no Processo Seletivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450152315
version: 11
---

Importante

Essa funcionalidade está disponível a partir da release 12.1.23.

Na página de inscrições do Processo Seletivo Web e na tela da Central do Candidato, será possível o envio de arquivos/documentos quando a área ofertada utilizar o recurso de exigir documentos no ato da inscrição e na página da central do aluno.

Será apresentada área para seleção de arquivo de acordo com sua exigência, pode ser obrigatória ou não.

**Parametrização:**

* Para habilitar o envio de arquivos o processo seletivo deverá ser configurado para indicar onde o arquivo será salvo, os tipos de arquivos aceitos e o tamanho máximo do arquivo.

Tamanho máximo de armazenamento (Kb)

Ressaltamos a importância do campo  **"Tamanho máximo de armazenamento (Kb)"**caso não seja preenchido ou seja indicado um valor igual a "0" será permitido enviar um arquivo de qualquer tamanho, no entanto existem configurações que podem ser definidas no IIS que também irão limitar o tamanho máximo de uma requisição (para maiores informações [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048818794-TOTVS-Educacional-Processo-Seletivo-Portal-Upload-de-arquivos-grandes-Envio-de-arquivos-erro-server-side)), e quando isso ocorrer não será apresentada uma mensagem intuitiva para o usuário final.  

Portanto recomendamos que esta informação seja preenchida, pois desta forma o sistema consegue tratar individualmente cada arquivo que será enviado apresentando ao usuário final uma mais coerente em relação ao tamanho do arquivo.

**Exemplo:**

* Após isso deverão ser informados tipos de arquivos solicitados que serão exibidos no portal. Para isso acesse o cadastro da Área de Interesse Ofertada, aba “Documento Exigido”, cadastre o arquivo/documento a ser solicitado.

Existem duas definições que serão consideradas:

**1 –** **Exibir na inscrição do Portal?:** Esse campo será responsável por definir se esse documento será exibido ou não na inscrição pelo portal. Caso sele esteja marcado o documento será exibido na tela de inscrição. Caso ele esteja desmarcado ele não será exibido.

**2 – Obrigatório**: Se este campo estiver marcado e o documento exibido no portal, o candidato só conseguirá realizar a sua inscrição se selecionar o arquivo na tela de inscrição.

Realizada essa parametrização a validação e envio de arquivos durante a inscrição e na central do aluno será exibida.

**Descrição do processo:**

Quando o candidato acessar a tela de inscrição, será verificado se existe algum documento a ser solicitado. Existindo documento solicitado o campo será exibido para o usuário no grupo “ENVIO DE DOCUMENTOS”. Se o arquivo for um arquivo obrigatório ele será exibido com um \* (asterisco) ao lado do texto “Enviar arquivo do documento”.

Caso o arquivo obrigatório não seja informado o campo será considerado inválido e o candidato não conseguirá finalizar a inscrição. Para arquivos não obrigatórios o candidato pode não enviar o arquivo.

Estando a seleção de arquivos atendida, ao clicar em Finalizar, será apresentada a tela de confirmação de matrícula onde será apresentado o grupo “ENVIO DE DOCUMENTOS”. Nesse grupo poderá ser visualizado no nome do arquivo selecionado para envio.

Finalizada a inscrição os arquivos enviados poderão ser visualizados no cadastro de alunos inscritos do processo seletivo.

**CENTRAL DO ALUNO**

Na Central do Aluno estes documentos serão exibidos para o usuário no grupo “ENVIO DE DOCUMENTOS”. Se o arquivo for um arquivo obrigatório ele será exibido com um \* (asterisco) ao lado do texto “Enviar arquivo do documento”. Se o arquivo já tiver sido validado pela instituição o usuário não poderá substituir o mesmo, sendo permitido apenas a realização do download. Caso ele não tenha sido validado o usuário poderá enviar um novo arquivo que irá sobrescrever o arquivo anterior.
