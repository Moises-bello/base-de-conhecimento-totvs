---
article_id: 360058603513
category: Financeiro - Borderô contas a Receber
content_hash: a95c8ba76cbaa6db7562762ede27b8e8de58db13bd8fd0b021cadd141d9610ed
fetched_at: '2026-06-28T22:37:39.723057+00:00'
product: protheus
section_id: 35057237655191
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA245 - Help: F245BANCOS'
type: support-article
updated_at: '2026-03-25T20:07:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058603513-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA245-Help-F245BANCOS
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39245488357399)***Tempo aproximado para leitura: **00:05:00 min**

**Ocorrência:**  
Ao realizar a geração do borderô automático pela na rotina **FINA245** apresenta o **Help**: F245BANCOS  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39245508231575)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**  
A ocorrência do **Help: F245BANCOS** ao realizar a geração do borderô automático pela rotina **FINA245** está relacionada a inconsistências ou ausência de preenchimento em cadastros essenciais do processo.

Esse comportamento pode ocorrer quando existem divergências ou campos não preenchidos corretamente no **cadastro de fornecedor**, **cadastro de bancos** ou **parâmetros bancários**.

Para solução, recomendamos validar os seguintes pontos:

No **Cadastro de Fornecedor (MATA020)**:  
Verifique o preenchimento do campo de banco na aba administrativa/financeira, garantindo que o campo **A2\_BANCO** esteja corretamente informado.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39245508233239)

Ainda no cadastro, acesse **Outras Opções > Banco**, onde ocorre o preenchimento manual da tabela **FIL**, utilizada nesse processo. Os campos abaixo devem estar devidamente preenchidos:

* Banco (FIL\_BANCO): Conteúdo pessoal determinado pelo usuário
* Agência (FIL\_AGENCI): Conteúdo pessoal determinado pelo usuário
* DV Agência (FIL\_DVAGE): Conteúdo pessoal determinado pelo usuário ou sem preenchimento
* Conta (FIL\_CONTA): Conteúdo pessoal determinado pelo usuário
* DV Conta (FIL\_DVCTA): Conteúdo pessoal determinado pelo usuário ou sem preenchimento
* **Tipo C/C (FIL\_TIPO) = 1 (Principal)**
* **C. de Detrac (FIL\_DETRAC) = Não pode estar sem preenchimento**
* **Tipo Conta (****FIL\_TICTA):** **Não pode estar sem preenchimento**
* **Permite C/C (FIL\_MOVCTO) = 1 (Sim)**  
  **![cadastro fil.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/39245488360599)**

Nos **Parâmetros de Banco (FINA130)**, valide os seguintes campos:

* Banco (EE\_CODIGO): Conteúdo pessoal determinado pelo usuário
* Agência (EE\_AGENCIA): Conteúdo pessoal determinado pelo usuário
* Conta (EE\_CONTA): Conteúdo pessoal determinado pelo usuário
* Sub Conta (EE\_SUBCONTA): Conteúdo pessoal determinado pelo usuário
* Extensão (EE\_EXTEN): Conteúdo pessoal determinado pelo usuário
* **Ret.Automát? (EE\_RETAUT) = AMBOS**
* Permite pgto (EE\_PERMPG) = S

![bancos.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/39245508234263)

Além disso, é fundamental garantir que as tabelas **FIL, SA2 e SE2** estejam com o **mesmo nível de compartilhamento**. Divergências nesse ponto também podem ocasionar a apresentação do Help.

****Importante****A manipulação da base de dados não é contemplada em nosso escopo de atendimento de Suporte Técnico, esse tipo de procedimento é efetuado apenas por analista in loco. Confira nosso Escopo  
 [Guia de Relacionamentos - Específico Protheus](%C2%A0https://tdn.totvs.com/pages/releaseview.action?pageId=547876496)

**Saiba Mais**  
[Borderô Automático (FINA245 - SIGAFIN)](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=312166157)  
[Exemplo do Processo de Borderô Automático (FINA245 - SIGAFIN)](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=312164184)
