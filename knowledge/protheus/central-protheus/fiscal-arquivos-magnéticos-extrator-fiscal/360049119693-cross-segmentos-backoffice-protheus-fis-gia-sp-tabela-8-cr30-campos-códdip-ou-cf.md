---
article_id: 360049119693
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 48b2fad7331d7f316f3b1af8ee1dda42eab95820ce4b429bf6d2c1fba8141cc3
fetched_at: '2026-06-28T22:42:07.956549+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - GIA-SP -  Tabela 8, CR=30, Campos
  - CódDIP ou CFOP inválidos
type: support-article
updated_at: '2024-06-10T19:20:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049119693-Cross-Segmentos-Backoffice-Protheus-FIS-GIA-SP-Tabela-8-CR-30-Campos-C%C3%B3dDIP-ou-CFOP-inv%C3%A1lidos
---

**Ocorrência**

Erro "**Tabela 8**, **CR=30**, - campos - **CódDIP** ou **CFOP** inválidos".

Erro "**Tabela 8**, **CR 30**, - campos -  **Q30**  ou **CFOP** inconsistente".

**Ambiente**TAF – Nova GIA – A partir da versão 12.1.17  
   
**Solução**

O erro "**Tabela 8**, **CR=30**, Campos - **CódDIP** ou **CFOP** inválidos" ocorre por não ter sido gerado o Registro **CR=30** no arquivo da **GIA-SP.**

Conforme,  **Página 32 do Manual da GIA**:

<https://portal.fazenda.sp.gov.br/servicos/gia/Downloads/pre_formatado_ngia_v0210_gia0801.pdf>  
  
Regra do **Manual da GIA**:

Para referência > 200212

Se houver lançamento no **CódDIP** 2.5

Condição 3 (\*\*)  
Se Existe **CFOP** 5.153, 6.153 ou 5.251 a 5.299 ou 6.251 a 6.299 ou 7.251 a 7.299  
Então,  
X = (BaseCálculo + IsentasNãoTrib + Outras) dos CFOP´s  
5.153, 6.153 E (5.251 a 5.299) e (6.251 a 6.299) E (7.251 a  
7.299)  
Se X > zero, Então  
Y = dos valores lançados nos Municípios para os  
CódDIP) CR=30 (DIPAM-B), com CódDIP = 2.5  
 Onde Y deve ser > zero e =< X

De acordo com a Regra da **Página da 32**, quando é utilizado **CFOP** na qual gera a **DIPAM-B**, deverá existir registros **CR=30**.

Segue abaixo um exemplo com o procedimento para a configuração nas **Notas Fiscais de Saídas** e **Notas Fiscais de Entrada.**

Como gerar o registro **CR=30** para **Nota Fiscal** de **Saídas** ou de **Entradas.**

- Inclua um cliente e Informe a **UF** (SP) e **Código do** **Município;**

- Inclua a **UF** para o qual será gerado o **CR30;**

- Informe no parâmetro **MV\_UFIPM = SP** (se a nota for gerada para essa UF);

- Baixe e importe a **Tabela IPM,** utilize o link:

<http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal>

- Importe a tabela pela rotina **FISA094**, informe o diretório do arquivo txt da tabela;

- Inclua uma **TES** e preencha o campo da **DIPAM**;

- Calcule **ICMS**;

- Informe o **CFOP** 5251 para o código **2.5**;

- Selecione o código de **DIPAM** e **UF** na grade inferior '**Índice de Participação dos Municípios**', **UF** e **Cod. IPM**(conforme imagem abaixo).

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072743373)

- Inclua a **Nota Fiscal** de Saída ou Entrada (espécie de energia elétrica - **NFCEE**) e utilize a TES criada**;**

- Efetue o complemento da nota;

- Execute a rotina do **Extrator Fiscal** para os *layouts* **T003**, **T005**, **T007**, **T009;**

- Execute a rotina do **Extrator Fiscal** para o *layout***T013**;

- Execute a rotina de **Processamento;**

- Gere o arquivo, informe o código de **DIPAM** e **CFOP** específico;

- Analise o campo **C30\_CODIPA**, se está alimentado com o código.

Para as **Notas Fiscais de Entrada**, considere o mesmo processo.

Caso as inconsistências persistam após as validações, abra uma solicitação para o **Suporte da Totvs.**
