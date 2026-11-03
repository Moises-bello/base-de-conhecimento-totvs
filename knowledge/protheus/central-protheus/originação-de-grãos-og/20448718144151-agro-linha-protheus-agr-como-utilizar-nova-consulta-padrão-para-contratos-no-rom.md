---
article_id: 20448718144151
category: Originação de Grãos (OG)
content_hash: 5b4352eff0e9da5ac5e0c2ea80b6cced5a60ed441b98301e25c72948f455bbbe
fetched_at: '2026-06-28T22:45:37.580641+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Como utilizar Nova Consulta Padrão para Contratos
  no Romaneio
type: support-article
updated_at: '2025-06-26T11:14:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20448718144151-Agro-Linha-Protheus-AGR-Como-utilizar-Nova-Consulta-Padr%C3%A3o-para-Contratos-no-Romaneio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20448718107415) Tempo aproximado para leitura: **00:01:25 min****Ocorrência**  
No módulo Comercialização (Linha Protheus) - Originação de Grãos (OG), ao realizar o procedimento para utilizar a nova consulta de contratos no romaneio é apresentada a ocorrência **Nova Consulta Padrão para Contratos no Romaneio**.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**  
Esse incidente ocorre, pois é necessário realizar o processo para utilizar a nova consulta de contratos no romaneio no Sistema.  
  
**Solução**Para utilizar essa nova funcionalidade é necessário por meio do **Configurador - SIGACFG** alterar a consulta padrão do campo da tabela **NJJ - NJJ\_CODCTR - código do contrato** e o campo da tabela **NJM - NJM\_CODCTR código do contrato**, para **NJJCTR**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20448701914263)

* Em **Gestão de Agronegócio (SIGAAGR)** acesse **Atualizações > Comercialização > Negociação*>*Contrato de Venda > Contrato de Venda;**
* Clique em **Incluir**;
* Informe os campos obrigatórios:
* Na pasta **Principal**: **(Entidade, Safra, Produto, TES)**;
* Na pasta **Previsão de Entrega (Quantidade)**;
* Na pasta **Dados Negócio/Financeiro** o campo **Tipo Fix. para "1 - Fixo" ou "2 - A Fixar"**.
* Clique em **Outras Ações > Composição de Preço.** Informe os valores para os componentes. Será apresentado o preço calculado. Informe então o campo **Preço Propost*o***. O Sistema exibirá o **Saldo da Margem**, ou seja, a diferença entre o **Proposto** e o que foi **Calculado**.
* Em seguida clique em **Salvar** e confirme a geração das informações do componente de preços. O valor que será considerado no contrato é o que foi digitado em **Preço Proposto.**
* Clique em **Confirmar**;
* Acesse **Outras Ações > Confirmar** para efetivar o contrato de venda.

Com o contrato confirmado e com preço fixado é possível visualizar as informações. Na pasta **Dados Negócio/Financeiro** do **Contrato de Venda** é exibido o valor total do contrato em **KG** e o valor unitário na unidade de medida de preço do contrato.
