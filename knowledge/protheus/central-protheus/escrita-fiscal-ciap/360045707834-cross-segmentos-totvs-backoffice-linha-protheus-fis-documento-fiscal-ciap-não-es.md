---
article_id: 360045707834
category: Escrita Fiscal - CIAP
content_hash: f19be31b9b34412dbd5ce8541e22532f4f3092bc130cf71c74843124a4e58041
fetched_at: '2026-06-28T22:39:33.901154+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Documento fiscal
  CIAP não esta sendo considerado na Apuração ICMS '
type: support-article
updated_at: '2021-07-29T11:57:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045707834-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Documento-fiscal-CIAP-n%C3%A3o-esta-sendo-considerado-na-Apura%C3%A7%C3%A3o-ICMS
---

**Dúvida**  
Documento Fiscal Ciap Não Esta Sendo Considerado na Apuração do ICMS  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Abaixo configurações de TES necessárias para inclusão do documento referente CIAP e gravação das informações na apuração do ICMS:

**TES:**  
•Credita ICMS = Sim

•Atu. Ativo = Sim – Caso haja integração com o módulo Ativo Fixo, o registro gerado na SF9 irá gerar um registro também na SN1.

•Desm. IT. ATF = Sim/Não – Campo utilizado para desmembrar os itens constantes na nota fiscal de entrada. Por exemplo: Item 001 – Quantidade: 03 – Se campo for configurado como SIM, serão criados 3 registros referentes a esta NF, caso configure como NÃO,será lançado somente um ativo com valor total de ICMS.

•CFOP = 1551 – Padrão.

•Calcula ICMS = Sim

•Livro Fiscal de ICMS = Outros

•Livro Fiscal CIAP =Sim

•Mat. Consumo = sim

•Trib. Ciap = Não - Considera as saídas tributadas, independente do Livro ICMS.

•Componente = Não – Considera se o bem será incluído no MATA905 como componente.

Se após configurar conforme acima, o documento fiscal não for apresentado na apuração, será necessário avaliar se o campo F3\_CODRSEF esta preenchido com o conteúdo 100 - Autorizado o uso da NF-e.

Caso esteja com o conteúdo 103 - Lote recebido com sucesso, será necessário que efetue o monitoramento da nota fiscal para que o código seja atualizado para "100" na tabela SF3 no campo F3\_CODRSEF.
