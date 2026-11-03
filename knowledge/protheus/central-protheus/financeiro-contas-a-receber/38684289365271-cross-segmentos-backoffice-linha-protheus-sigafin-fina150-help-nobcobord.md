---
article_id: 38684289365271
category: Financeiro - Contas a Receber
content_hash: 4f30ef49d7f4483b542674d3541663b726c181a492229dcc58242a695993f1ee
fetched_at: '2026-06-28T22:38:13.980219+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA150 - Help: NOBCOBORD'
type: support-article
updated_at: '2026-03-30T13:47:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38684289365271-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA150-Help-NOBCOBORD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38684311532439) Tempo aproximado para leitura: 00**:05:00 min**  
  
**Dúvida**  
Ao processar a rotina de Geração de Arquivo de Cobrança (Remessa) no módulo Financeiro, o sistema Protheus apresenta a mensagem de **Help NOBCOBORD**.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS SIGAFIN - Todas as versões  
  
**Solução**  
Este bloqueio ocorre quando o sistema identifica que o borderô selecionado para o processamento está atrelado a uma combinação de Banco, Agência e Conta diferente daquela que está sendo informada para a geração do arquivo.

O Protheus executa uma validação padrão para garantir a integridade da remessa bancária. Ele cruza as informações preenchidas pelo usuário com os dados efetivos do título no banco de dados. O Help será acionado nas seguintes situações:

1. **Inconsistência de Cadastro Básico:** A chave formada pelo "Banco + Agência + Conta" parametrizada na tela de geração do arquivo difere da chave real gravada no registro do borderô (campos `EA_PORTADO`, `EA_AGEDEP` e `EA_NUMCON` da tabela `SEA`).
2. **Bloqueio por Customização (Ponto de Entrada):** Caso exista o Ponto de Entrada `F150BBCO` compilado no seu ambiente e a lógica interna dele retorne falso (`.F.`), o sistema automaticamente acionará o Help, mesmo que os dados do banco pareçam corretos.

Para sanar a ocorrência do Help **NOBCOBORD**, siga estas etapas:

* Confirme se o Banco, Agência e Conta informados correspondem rigorosamente aos dados do(s) borderô(s) que você deseja transmitir.
* Verifique o conteúdo dos campos de Portador (`EA_PORTADO`), Agência (`EA_AGEDEP`) e Conta (`EA_NUMCON`). O conteúdo dessa trinca precisa ser idêntico ao informado nos parâmetros da remessa.
* Peça para verificarem o Ponto de Entrada `F150BBCO`. Se esta customização existir e estiver retornando o valor lógico falso (`.F.`) para o título ou lote em questão, o sistema interpretará como um bloqueio manual e emitirá o Help. A regra do código customizado precisará ser ajustada para retornar `.T.` nas condições aceitas pela empresa.

**Saiba mais:**

[**F150BBCO - Valida o banco utilizado para geração do arquivo**](https://tdn.totvs.com/pages/viewpage.action?pageId=180584877)
