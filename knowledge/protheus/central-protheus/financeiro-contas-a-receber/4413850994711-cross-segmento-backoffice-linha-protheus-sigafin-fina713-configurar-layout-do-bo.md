---
article_id: 4413850994711
category: Financeiro - Contas a Receber
content_hash: c554953065220c2cf43a14d3a94227c01d0f7293b898dd8589d65063b838712d
fetched_at: '2026-06-28T22:38:12.859673+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA713 -  Configurar
  layout  do Boleto via API - Novo painel gestor
type: support-article
updated_at: '2024-12-04T18:28:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413850994711-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Configurar-layout-do-Boleto-via-API-Novo-painel-gestor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15366733313815) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Como configurar o novo layout do boleto via API no Novo Painel Gestor Financeiro?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – FINA713 - A partir da versão 12.1.33  
  
**Solução**Primeiramente, para mostrar o banco no novo painel de gestor, será preciso configurar alguns campos no cadastro de bancos e os parâmetros do banco.

**Cadastro de Bancos:**

* + Preencher o campo **"Fluxo de Caixa"** com a opção **"Sim"**.
  + No campo **"Banco Oficial"**, informar o **número do banco** e o **país da conta**.

**Cadastro de Parâmetros de Banco:**

* O campo **"Nosso Número"** deve ser parametrizado nos seguintes campos. Exemplo:
  + **Faixa Início** (00000000)
  + **Faixa Fim** (99999999)
  + **Faixa Atual** (00000001)

**Observação**  
Cada instituição bancária possui particularidades específicas. É necessário consultar a documentação abaixo para validar os campos obrigatórios.

**Link com os bancos Homologados:**

[Contas a receber (Comunicação bancária online) - Bancos Homologados](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392)

**Importante**

Caso o banco cadastrado contenha caracteres especiais, como ilustrado no exemplo a seguir, poderá ocorrer erro no envio do boleto, impedindo sua transmissão ao banco.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/28278057655831)**

Para evitar inconsistências em outros processos e consultas no sistema, no cadastro de parâmetros de banco, na aba **"Outros"**, é fundamental preencher corretamente os dados da agência e da conta nos campos apropriados. Dessa forma, o sistema passará a desconsiderar a aba **"Cadastrais"** do banco, passando a considerar as informações inseridas na aba **"Outros"**.

**![Gravar_2024_12_04_14_56_52_146.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/28278008236055)**

**Configurando o Layout**

* No novo Painel Gestor Financeiro, acesse, **Comunicação Online,** em seguida, **Configuração de Contas**, Clicar em **Novo Layout.**
* ![Gravar_2024_12_04_15_13_42_243.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/28278057661335)

O layout também apresenta particularidades no preenchimento inicial, as quais envolvem as credenciais do banco.

Para os bancos que exigem os arquivos-chave do certificado KET e CRT, estes devem ser adicionados na pasta **Protheus Data\cert\ngf**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28278008242199)

O nome do arquivo deve coincidir com o especificado na configuração do layout, devendo ser escrito em letras minúsculas.

Por fim, configure as demais informações, como juros, multa, desconto, entre outras, conforme as necessidades da empresa.![Gravar_2024_12_04_15_21_38_403.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/28278008243991)

**Saiba mais**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Não foi possível gerar os arquivos corretamente Erro ao extrair o Certificado de Autorização no CFGX060 Wizard de Conversão de Certificado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10621741400087-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-N%C3%A3o-foi-poss%C3%ADvel-gerar-os-arquivos-corretamente-Erro-ao-extrair-o-Certificado-de-Autoriza%C3%A7%C3%A3o-no-CFGX060-Wizard-de-Convers%C3%A3o-de-Certificado?source=search)

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Como Exportar e Aumentar o tamanho do arquivo .PFX ( Certificado Digital - modelo A1 )](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10811119314199-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Como-Exportar-e-Aumentar-o-tamanho-do-arquivo-PFX-Certificado-Digital-modelo-A1)
