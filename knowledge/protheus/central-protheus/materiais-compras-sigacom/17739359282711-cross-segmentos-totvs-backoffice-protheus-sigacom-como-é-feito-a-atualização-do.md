---
article_id: 17739359282711
category: Materiais - Compras (SIGACOM)
content_hash: fbdb9da367e3c868462bc480cb681c8d3aaddffdc8ec73fa5273f470f6377ba8
fetched_at: '2026-06-28T22:41:15.790252+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é feito a atualização
  do status no Portal do Transmite quando inserido no documento de entrada?
type: support-article
updated_at: '2024-04-02T14:16:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17739359282711-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-feito-a-atualiza%C3%A7%C3%A3o-do-status-no-Portal-do-Transmite-quando-inserido-no-documento-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17739374888087) Tempo aproximado para leitura: 00:04 min **Dúvida**

Como é feito a atualização do status dos documentos quando inserido diretamente no Protheus via rotina Documento de Entrada e/ou Pré-Nota quando há integração com o TOTVS Transmite.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - VERSAO 12

**Solução**

Em algumas situações é necessário atualizar o status de um documento no TOTVS Transmite que foi inserido via EDI e/ou manualmente através da rotina Documento de Entrada e/ou Pré-Nota.

Abaixo segue como feito a atualização de status do documento no TOTVS Transmite, quando for inserido via EDI e/ou manualmente.

 **Passo 1:** Incluir o documento via Documento de Entrada ou Pré-Nota.

* Utilize a rotina de Documento de Entrada ou Pré-Nota para inserir o documento.

**Passo 2:** O sistema irá realizar a Importação do XML que consta no Portal do Transmite.

* Aguarde que o XML correspondente ao documento inserido via Documento de Entrada seja importado pelo Importador XML para o Monitor do TOTVS Transmite.

**Passo 3:** Verificação do documento no Monitor.

* Acesse o Monitor do TOTVS Transmite e verifique se o documento importado (**ex: 0000001/001**) está listado corretamente.

**Passo 4:** Geração do documento no Monitor.

* Selecione o documento desejado (**ex: 0000001/001**) no Monitor e clique na opção "Gerar documento" para atualizar o status para "Documento Gerado".

**Passo 5:** Repetição do processo para outros documentos.

* Repita os passos 1 a 4 conforme necessário para todos os documentos que precisam ter seu status atualizado no TOTVS Transmite.

**Passo 6:** Aguardar a próxima sincronização/requisição de documentos

* Após ter concluído a atualização de status para todos os documentos necessários, aguarde até a próxima sincronização ou requisição de documentos entre o Importador XML e o TOTVS Transmite.

**Passo 7:** Verificação e atualização automática de status

* Durante a próxima sincronização/requisição de documentos, o TOTVS Transmite analisará e verificará quais documentos já foram integrados e atualizará automaticamente o status de acordo com as informações fornecidas pelo Importador XML.

***Saiba Mais:***

[Integração Importador XML x TOTVS Transmite](https://tdn.totvs.com/pages/releaseview.action?pageId=678583195)

[Status de documento no TOTVS Transmite quando inseridos via Documento de Entrada](https://tdn.totvs.com.br/display/public/PROT/IX08014+-+Importador+XML+x+TOTVS+Transmite+-+Status+de+documento+no+TOTVS+Transmite+quando+inseridos+via+Documento+de+Entrada)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
