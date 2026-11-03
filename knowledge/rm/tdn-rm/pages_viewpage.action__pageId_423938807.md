---
content_hash: 5e978fdaf3a1a387f4322c832df13fe925e15a6349a2fc2884a285855598172b
fetched_at: '2026-06-29T00:09:29.098374+00:00'
page_id: '423938807'
product: rm
source: tdn-rm
title: Prestação de Serviço em Desacordo (CT-e/CT-e OS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938807
version: 3
---

Este evento serve para que o tomador possa informar ao fisco que o documento CT-e/CT-e OS que o relaciona está em desacordo com a prestação de serviço CT-e de Transporte de Cargas (modelo 57 e 67).  
O autor do evento é o tomador do serviço indicado no CT-e/CT-e OS.   
A mensagem XML do evento será assinada com o certificado digital que tenha o CNPJ base do tomador do serviço do CT-e/CT-e OS.   
Para utilização desse processo, acessar o cadastro de filial no caminho Cadastros | Filial. Selecionar a Filial para o qual deseja enviar a Prestação em Desacordo e acessar o Anexos | Prestações em Desacordo(CT-e/CT-e OS).  
Clicar no botão Incluir e preencher a Chave de Acesso e a Observação da Prestação em Desacordo na Tela.  
***Observação***: O campo Tipo de Documento é automaticamente preenchido de acordo com a chave de acesso informada.   
Após salvar o registro, selecionar o mesmo e, com o TSS aberto, ir em Processos | Enviar Prestação em Desacordo.   
Esse processo irá enviar o registro para a SEFAZ, e modificará o status do registro para Pendente.   
Em seguida, selecionar o registro com Status Pendente e, com o TSS aberto, ir em Processos | Consultar Prestação em Desacordo.Após a consulta, a SEFAZ retornará se a Prestação em Desacordo foi vinculada com sucesso ao CT-e ou CT-e OS, o que mudará o registro para o Status de Autorizado.   
Se houver alguma inconsistência que impediu a Autorização o registro ficará com status de Rejeitado.

* [Evento de Prestação de Serviço em Desacordo](http://tdn.totvs.com/pages/viewpage.action?pageId=351017018)
