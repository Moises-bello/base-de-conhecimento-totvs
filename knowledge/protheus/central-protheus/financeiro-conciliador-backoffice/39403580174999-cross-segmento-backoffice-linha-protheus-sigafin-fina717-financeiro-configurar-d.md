---
article_id: 39403580174999
category: Financeiro - Conciliador Backoffice
content_hash: 6e27ab25d52e9ceadf9b4b96a6550726e18d6622f73893147f1f24842c4d649d
fetched_at: '2026-06-28T22:37:47.049958+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA717 - Financeiro
  - Configurar dados bancários do fornecedor no envio de boleto online a pagar
type: support-article
updated_at: '2026-05-22T17:08:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39403580174999-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA717-Financeiro-Configurar-dados-banc%C3%A1rios-do-fornecedor-no-envio-de-boleto-online-a-pagar
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39403609806231) Tempo aproximado para leitura: **00:15:00 min**  
  
Como configurar e validar a origem dos campos de banco, agência e conta do fornecedor para que sejam importados corretamente no envio do pagamento ao banco?

Ambiente

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro (SIGAFIN) - Todas as versões

Solução

Para que os dados bancários do fornecedor sejam carregados corretamente na integração via API, a rotina de Configuração de Contas precisa estar com os campos de "Transferência" (Banco, Agência e Conta de Crédito) apontando para os campos corretos da base de dados do Protheus.

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39463451097623)

Passos

1. Acesse o Novo Gestor Financeiro e navegue até "Comunicação Online > Configuração de Contas", localize a conta do banco configurado para a modalidade "API Pagar" (transmissão de pagamentos), clique em "..." e depois em "Editar".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39463463593751)

2. Na tela de configurações, role para baixo até a seção "Transferência", verifique a configuração dos campos que determinam a origem dos dados bancários do fornecedor. Certifique-se de que eles estão apontando para os campos corretos:

Exemplo indicando as informações presentes no título (SE2).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39463451097623)

3. Após a alteração, clique em "Salvar Alteração".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39463451098391)

**Saiba mais**

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/20980892258071-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-FINA717-Help-Opera%C3%A7%C3%A3o-n%C3%A3o-permitida-pois-o-boleto-n%C3%A3o-pertence-ao-conv%C3%AAnio-do-usu%C3%A1rio>

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/18694324704919-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA717-Erro-ao-transmitir-Falha-na-comunica%C3%A7%C3%A3o-com-o-Banco-do-Brasil>

How To l SIGAFIN - FINA717 - Cadastro JOB e Transmissão do Título

<https://www.youtube.com/watch?v=rgnYexReqq4>
