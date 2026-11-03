---
article_id: 11946241656983
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: fbd4d377d11f547df5263da645821af2f0b17fa92b7274735fd96bf9f2066af6
fetched_at: '2026-06-28T22:42:01.181793+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar o registro 1601?
type: support-article
updated_at: '2023-11-21T12:05:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11946241656983-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-o-registro-1601
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar o registro **1601 - Operações com Instrumentos de Pagamentos Eletrônicos** no arquivo magnético **do Sped Fiscal?**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

O registro **1601** pode ser gerado de forma automática através módulo **SIGALOJA** ou através da utilização do ponto de entrada **SPED1601.**Para geração do registro via módulo **SIGALOJA,** é preciso realizar o seguinte procedimento:

1. Cadastre as **Administradoras Financeiras**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11945831488919)  
**Tipo Adminstr=CC** - para cartão de crédito, ou **DB**  para cartão de débito.  
  
2. Rede Destino = **Selecione a empresa administradora** – esse campo é responsável para geração do registro **1600** unificado das **administradoras** **financeiras**.  
  
**Importante:**

Ao criar um cadastro na Tabela **SAE - Administradora Financeira**, o sistema cria o mesmo cadastro na tabela **SA1 - Clientes,** para preencher os dados e gerar o registro **0150 - Tabela de Cadastro do Participante** corretamente;  
  
3. Verifique o cadastro de **Administradoras (tabela SAE).** Obrigatoriamente todos cadastros devem ser preenchidos corretamente;

**Campos:**  
**- Tipo Admins (AE\_TIPO);**  
**- Rede Destino (AE\_REDE)**, informe a rede para que o sistema gere corretamente. Caso não exista, efetue o cadastro na **tabela genérica L9** via **Configurador**.  
  
4. Preencher no campo **AE\_CODCLI/AE\_LOJCLI** com o código do cliente referente a administradora financeira .  
  
5. No cadastro de cliente, todas  as administradoras devem possuir o cadastro completo: **Endereço**, **código de municípios**, **UF**, **bairro**, **CNPJ**, **inscrição** **estadual**, **país**, **etc.**  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11946090829847)  
  
6. Gere o **cupom**, no passo do **F7**, clicar na opção **Zerar Pagamentos** e depois selecionar **Cartão de Crédito**  
  
**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11946095352343)**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11946134218519)**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11946134766743)

Dessa forma o **Protheus** gera as informações na tabela **SL4**, de onde busca os dados para o registro **1601**, de acordo com os dados dos campos selecionados abaixo:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11946149651223)

7. Na *wizard* do **SPEDFISCAL,** as perguntas **Gera Registro de ECF** e **Gera Registro 1601** devem estar como **SIM**  
  
**![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11946151827479)**

**![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11946175573399)**

Para geração do registro via **ponto de entrada,** siga as orientações do *link* abaixo: <https://tdn.totvs.com/pages/releaseview.action?pageId=651921344>
