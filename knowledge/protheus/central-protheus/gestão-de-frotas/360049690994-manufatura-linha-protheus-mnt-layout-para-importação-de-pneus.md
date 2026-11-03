---
article_id: 360049690994
category: Gestão de Frotas
content_hash: 3224c6aafff236dc37ef537b7491e12a4a72edd08a43cc860ae074e963fe52ef
fetched_at: '2026-06-28T22:42:39.498565+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Layout para importação de Pneus
type: support-article
updated_at: '2021-08-13T18:20:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049690994-Manufatura-Linha-Protheus-MNT-Layout-para-importa%C3%A7%C3%A3o-de-Pneus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png) Tempo aproximado para leitura: **00:07:20 min**  
**Dúvida**Qual é o *layout* para importação de **Pneus**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - A partir da versão 12  
  
**Solução**Segue abaixo o *layout* para importação de **Pneus** via arquivo **.txt** na rotina **Importação de Pneus - MNTA998**.

| Pos. | Coluna | Tipo | Tam. | Dec. | Obg. | Descrição | Formato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **1** | **T9\_FILIAL** | **C** | **2-12** |  | **X** | **Código da Filial** | 999999999999 - não utilizar aspas no arquivo importado.  O tamanho do campo no arquivo segue o tamanho do campo **M0\_CODFIL - Filial** no dicionário referente à tabela **SM0 - Empresa**. Possui **grupo de campo** e o tamanho varia de **2 à 12**. |
| **2** | **T9\_CODBEM** | **C** | **10** |  | **X** | **Código do pneu ou número de fogo** | No caso do pneu poderá ser iniciado com **P+Número** de fogo do pneu. Possui tamanho **menor** que o do **Código do Bem** na rotina de **Pneus**, pois este campo será gravado também no **número de fogo** que é tamanho 10. |
| **3** | **T9\_CODFAMI** | **C** | **6** |  | **X** | **Código da família de pneus** | **Exemplo: LS-97, R250, XZY, T-546, G-167** O tamanho do campo no arquivo importado segue o tamanho do campo **T6\_CODFAMI - Código Família**no dicionário referente à tabela **ST6 - Família.** |
| **4** | **T9\_NOME** | **C** | **40** |  | **X** | **Código da família de pneus** | Pode ser composto pelo **modelo + Fabricante + medida**  **Exemplo: G-358 GOODYEAR 295/80R22,5** O tamanho do campo **T9\_NOME - Nome** segue o tamanho do dicionário e se refere à tabela **ST9 - Bem.** |
| **5** | **T9\_CCUSTO** | **C** | **9** |  |  | **Código do Centro de Custo** | Somente **obrigatório** se o pneu **não** for aplicado. O tamanho do campo no arquivo importado segue o tamanho do **CTT\_CUSTO - Centro de Custo** no dicionário referente à tabela **CTT - Centro de custo** Possui **grupo de campo**e o tamanho varia de **9 à 20.** |
| **6** | **T9\_TIPMOD** | **C** | **10** |  | **X** | **Tipo Modelo do Bem** | Modelo do bem ou Modelo original do pneu. **Exemplo: XZA, XZY, etc.** O tamanho do campo no arquivo importado segue o tamanho do **TQR\_TIPMOD - Tipo Modelo** no dicionário referente à tabela **TQR - Tipo modelo.** |
| **7** | **T9\_SERIE** | **C** | **15** |  |  | **Serie do Pneu** | Campo texto sem validação O tamanho do campo no arquivo importado segue o tamanho do campo **T9\_SERIE - Série** no dicionário referente à tabela **ST9**. |
| **8** | **T9\_FABRICA** | **C** | **6** |  |  | **Código do Fabricante do pneu** | Campo alinhado a esquerda. O tamanho do campo no arquivo importado segue o tamanho do campo **T9\_FABRICA - Fabricante** no dicionário referente à tabela **ST9.** |
| **9** | **T9\_DTCOMPR** | **D** | **10** |  | **X** | **Data da compra** | **DD/MM/AAAA - Dia mês e ano** |
| **10** | **T9\_ESTRUTU** | **C** | **1** |  |  | **Indicador de Estrutura** | **N** Não utilizar aspas no arquivo |
| **11** | **T9\_TEMCONT** | **C** | **1** |  |  | **Tem contador - controlado pelo Pai** | **P** Não utilizar aspas no arquivo Se não for informado ele usará como valor padrão o **P - Controlado pelo Pai da estrutura.** |
| **12** | **T9\_TPCONTA** | **C** | **9** |  |  | **Tipo de contador** | **HODOMETRO** Não utilizar aspas no arquivo. |
| **13** | **T9\_POSCONT** | **N** | **9** |  | **X** | **Posição do Contador do Pneu** | Separar as casas decimais por **. - Ponto** Não é necessário completar o tamanho. Se for 1 utilizar apenas 1. O tamanho do campo no arquivo texto segue o tamanho do campo **T9\_POSCONT - Posição Contador** no dicionário referente à tabela **ST9.** |
| **14** | **T9\_DTULTAC** | **D** | **10** |  | **X** | **Data do último acompanhamento do contador** | **DD/MM/AAAA - Dia mês e ano** |
| **15** | **T9\_VARDIA** | **N** | **6** |  | **X** | **Variação dia** | Média de variação dia do **KM - Quilômetro** do pneu. Se não tiver pode informar fixo igual a 100. O tamanho do campo no arquivo importado segue o tamanho do campo **T9\_VARDIA - Variação Dia** no dicionário referente à tabela **ST9**. |
| **16** | **T9\_LIMICON** | **N** | **6** |  | **X** | **Limite do Contador** | **999999** separando as casas decimais por ponto. O tamanho do campo no arquivo texto segue o tamanho do campo **T9\_LIMICON - Limite Contador** no dicionário referente à tabela **ST9**. |
| **17** | **T9\_CONTACU** | **N** | **9** |  | **X** | **Contador acumulado do pneu** | Posição do contador de **KM** rodados do pneu. O tamanho do campo no arquivo importado segue o tamanho do campo **T9\_CONTACU - Contador Acumulado** no dicionário referente à tabela **ST9**. |
| **18** | **T9\_SITMAN** | **C** | **1** |  | **X** | **Situação Manutenção** | **A** Não utilizar aspas no arquivo texto. |
| **19** | **T9\_SITBEM** | **C** | **1** |  | **X** | **Situação do Bem** | **A** Não utilizar aspas no arquivo texto. |
| **20** | **T9\_CONTDES** | **C** | **1** |  |  | **Tipo controle vida útil - Contador ou Tempo** | **C** Não utilizar aspas no arquivo texto. |
| **21** | **T9\_VALCPA** | **N** | **12** | **2** |  | **Valor de compra do pneu** | **999999999.99** - onde as casas decimais devem ser separadas por ponto. O tamanho do campo no arquivo texto segue o tamanho do campo **T9\_VALCPA - Valor de Compra** no dicionário referente à tabela **ST9.**Se não for informado ele usará como valor padrão o **0 - Zero**. |
| **22** | **T9\_CODESTO** | **C** | **15** |  |  | **Código do pneu no estoque** | O tamanho do campo no arquivo importado segue o tamanho do campo **B1\_COD - Código** no dicionário referente à tabela **SB1 - Produto**.  Possui **grupo de campo** e o tamanho varia de **15 à 30**. |
| **23** | **TQS\_MEDIDA** | **C** | **6** |  | **X** | **Código da Medida do pneu** | O tamanho do campo no arquivo importado segue o tamanho do campo **TQT\_MEDIDA - Medida** no dicionário referente à tabela **TQT - Medida**. |
| **24** | **TQS\_SULCAT** | **N** | **6** | **2** | **X** | **Prof. Sulco Atual** | 999,99  O tamanho do campo no arquivo importado segue o tamanho do campo **TQS\_SULCAT - Profundidade Sulco** no dicionário referente à tabela **TQS - Medidas bem**. |
| **25** | **TQS\_DTMEAT** | **D** | **10** |  | **X** | **Dt Med. Sulco Atual** | **DD/MM/AAAA - Dia mês e ano** |
| **26** | **TQS\_HRMEAT** | **C** | **5** |  | **X** | **Hr. Med. Sulco Atual** | **99:99** |
| **27** | **TQS\_BANDAA** | **C** | **1** |  | **X** | **Código da Banda Atual** | **1=OR; 2=R1;3=R2;4=R3;5=R4** |
| **28** | **TQS\_DESENH** | **C** | **10** |  |  | **Código do Desenho** | **Modelo da Banda** atual do **Pneu**. Se for banda **original**, este campo **deve** ficar em branco. Caso seja banda **diferente** de **original** informar o **código** do **desenho**. O tamanho do campo no arquivo texto segue o tamanho do campo **TQU\_DESENH - Desenho** no dicionário referente à tabela **TQU - Desenho.** |
| **29** | **TQS\_KMOR** | **N** | **9** |  |  | **Km banda Original** | Km percorridos na banda Original |
| **30** | **TQS\_KMR1** | **N** | **9** |  |  | **Km banda R1** | Km percorridos na banda **R1** |
| **31** | **TQS\_KMR2** | **N** | **9** |  |  | **Km banda R2** | Km percorridos na banda **R2** |
| **32** | **TQS\_KMR3** | **N** | **9** |  |  | **Km banda R3** | Km percorridos na banda **R3** |
| **33** | **TQS\_KMR4** | **N** | **9** |  |  | **Km banda R4** | Km percorridos na banda **R4** |
| **34** | **TQS\_DOT** | **N** | **4** |  | **X** | **Data de Fabricação** | Semana e ano data fabricação no formato **SSAA - Semana e ano** |
| **35** | **TQS\_PLACA** | **C** | **8** |  |  | **Placa da frota** | Placa do **Bem/Veículo** onde está aplicado o **Pneu** O tamanho do campo no arquivo importado segue o tamanho da **T9\_PLACA - Placa** no dicionário referente à tabela **ST9**. |
| **36** | **TQS\_EIXO** | **N** | **1** |  |  | **Número do Eixo** | O tamanho do campo no arquivo importado segue o tamanho do campo **TQS\_EIXO - Eixo** no dicionário referente à tabela **TQS.** |
| **37** | **TQS\_POSIC** | **C** | **6** |  |  | **Código da Posição** | Posição onde o pneu está localizado O tamanho do campo no arquivo importado segue o tamanho do campo **TPS\_CODLOC - Local** no dicionário referente à tabela **TPS - Local**. |
| **38** | **TQS\_TIPEIX** | **C** | **1** |  |  | **Tipo de Eixo** | **Tipo do Eixo Opções:  1 - Livre; 2 - Tracionador; 3 - Direcional; 4 - Direcional/Tracionador.** |
| **39** | **T9\_STATUS** | **C** | **2** |  | **X** | **Status do Pneu** | Código do status atual do pneu.  Exemplo **01 - Aplicado ao parâmetro MV\_NGSTAPL** O tamanho do campo no arquivo importado segue o tamanho do campo **TQY\_STATUS - Status** no dicionário referente à tabela **TQY - Status**. |
| **40** | **T9\_LOCPAD** | **C** | **6** |  |  | **Código do Almoxarifado** | Código de almoxarifado referente ao produto de estoque vinculado ao pneu. O tamanho do campo no arquivo importado segue o tamanho do campo **NNR\_CODIGO - Código do Local** no dicionário referente à tabela **NNR - Local**.  Possui **grupo de campo**e o tamanho varia de **2 à 6.** |

**Importante**  
Cada campo do arquivo deve ser separado através da tecla **TAB**. A tabulação é que faz com que a rotina entenda quais campos estão sendo importados.  
  
**Saiba mais**Para verificar os **PE - Pontos de Entrada** dessa rotina, verifique os *links*:  
[Indica quantas colunas extras serão adicionadas na importação de pneus](https://tdn.totvs.com.br/pages/releaseview.action?pageId=6793760)  
[Permite a validação de novas colunas ou de colunas já existentes](https://tdn.totvs.com.br/pages/releaseview.action?pageId=6793761)  
[Grava na tabela TQS as colunas extras, adicionadas pelo usuário no TXT](https://tdn.totvs.com.br/pages/releaseview.action?pageId=6793762)  
  
**Anexo**  
Segue um modelo que pode ser utilizado como exemplo para montagem do arquivo importado.
