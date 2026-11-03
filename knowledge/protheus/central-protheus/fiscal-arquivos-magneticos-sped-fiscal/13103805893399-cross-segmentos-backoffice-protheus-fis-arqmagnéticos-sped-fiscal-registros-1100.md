---
article_id: 13103805893399
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 98ec3ffb007a451e1ff19ae9e2958b0dbad899b63b10df611cf6ca06cf1ff149
fetched_at: '2026-06-28T22:42:03.646315+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal
  - Registros 1100 e 1105 não gerados no Sped Fiscal.
type: support-article
updated_at: '2023-03-15T17:01:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13103805893399-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Registros-1100-e-1105-n%C3%A3o-gerados-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **03:00 min** **Dúvida**O que avaliar quando os registros **1100 - Informações sobre Exportação** e **1105 - Documentos Fiscais de Exportação** não forem gerados no **Sped Fiscal**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**1. Caso as notas  de exportação sejam geradas pelo módulo **05 - Faturamento** verifique se o campo **Data de averbação - CDL\_DTAVB** está preenchido para as notas fiscais que não estão gerando nos registros.  
   
O **Protheus** leva em consideração este campo como principal com relação as datas. Caso não esteja preenchido, como solução acesse o caminho abaixo e preencha o campo:  
   
**Livros Fiscais>Atualizações>Movimentos>NF Manual de Saída>Outras ações>Complementos> Exportações.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13106763956119)  
 

2. Se as notas são geradas via módulo **Easy Export Control - SIGAECC**, os registros **(1100, 1105** e **1110)** são gerados com base nas tabelas **EE7, EE8, EE9, EEC** e **EXL**.

Dessa forma é preciso verificar as informações abaixo:

**MV\_EECFAT:= .T.**  
**MV\_EECSPED:= .T.**

**MV\_EEC0001 = define se irá buscar a data de embarque ou averbação**  
**Parâmetro** que vai interferir na Geração do Registro **1100**, onde o fonte faz 2 tipos de busca para Geração das NF de **Exportação**. O Fonte **SPED FISCAL** faz uma chamada em 2 funções no **fonte AVGERAL**, para geração destes registro.  
   
A função **AvGetExpSped** é responsável por carregar os dados que serão enviados ao **SPED Fiscal**. Para isso temos dois cenários:  
· **Parâmetro MV\_EEC0001 = 1** - O sistema irá considerar a **data de embarque** do processo para carregar os dados a serem enviados ao **SPED Fiscal**.  
· **Parâmetro MV\_EEC0001 = 2** - O sistema irá considerar a **data de averbação** dos itens do processo para carregar os dados a serem enviados ao **SPED Fiscal**.  
   
**Nome da Variável := MV\_EEC0001**  
**Tipo := C**  
**Descrição := Define o campo a ser utilizado como parâmetro para geração dos dados a serem enviados ao SPED.**  
**Valor Padrão := 1= Data de Embarque; 2= Data de Averbação.**  
   
Lembrando se a NF de exportação ter sido embarcada com sucesso, gerar informações nas Tabelas **EE9 - Itens Embarque e EEC - Embarque**. Somente parâmetro irá interferir na Geração deste registro.  
   
Preencha com o conteúdo utilizado com o conceito utilizado pela sua organização.  
   
Para que os dados da **DU-E (Declaração Única de Exportação)** sejam enviados para o registro **1100**  
avalie os campos:  
**EEC\_NRODUE, EEC\_NRORUC, EEC\_DTDUE e EEC\_VMINGE e EXL\_AVRBDS** e verifique se as informações são enviadas para o Registro **1100**  
É obrigatório o preenchimento do campo **EE9\_DTAVRB** (**MV\_EEC0001 = 2**), sem essa informação os dados não são enviados ao **SPED Fiscal**.  
O campo **EEC\_VMINGE** só é usado quando há **integração com a DU-E**, caso o usuário informe manualmente os dados da **DU-E** este campo não será preenchido, pois é visual.  
   
Quando a nota é emitida pelo **SIGAEEC,** o sistema cria uma **tabela temporária** com todos esses dados para o preenchimento do registro, segue regra abaixo, onde o sistema busca os conteúdos para alimentar a tabela temporária e cada campo.  
   
**Campo 2 -****IND\_DOC** é preenchido através das tabelas **EE9** e **EXL**  
Se o campo **EE9\_NRSD** e o campo **EXL\_DSE** estiverem vazios, o sistema não irá preencher o campo 02.  
   
Se **EE9\_NRSD** estiver preenchido, então o campo **2 -****IND\_DOC** é preenchido com **0**.  
   
Se o campo **EXL\_DSE** estiver preenchido, então o campo **2 -****IND\_DOC** é preenchido com **1.**  
   
**Campo 03-** **NRO\_DE** utiliza as mesmas tabelas e validações que o campo 02  
A diferença é que este campo será preenchido com o conteúdo do campo  
**EE9\_NRSD** ou **EXL\_DSE** dependendo de qual está preenchido.  
   
**Campo 04** **DT\_DE** usa a mesma validação do campo 02  
Caso o campo **EE9\_NRSD** estiver preenchido, carrega o conteúdo do campo **EE9\_DTDE**, se não estiver preenchido, pega o conteúdo do campo **EXL\_DTDSE.**  
Caso os campos **EE9\_NRSD** e **EXL\_DSE** os campos 2, 3 e 4 ficaram vazios  
**Campo 04** Registro **1105**: Precisa que as tabelas **EEM** e **SF2** estejam preenchidas, o campo 04 é preenchido com o conteúdo do campo **EEM\_NRNF**.  
   
**Campo 06**Registro **1105** é preenchido com o campo **EEM\_DTNF.**  
**Campo 09** do registro **1100** - **DT\_CHC** é preenchido com o conteúdo do campo **EEC\_DTCONH**  
**Campo 10** do registro **1100** é preenchido com o campo **EXL\_AVRBDS** ou **EE9\_DTAVRB**  
   
*Query*:  
O campo **EXL\_AVRBDS** precisa existir em seu ambiente  
   
Se MV\_EEC0001 = 1:  
Select R\_E\_C\_N\_O\_ as EEC\_RECNO  
From EECxxx  
Where D\_E\_L\_E\_T\_ <> '\*'  
And EEC\_FILIAL = 'Código da sua filial'  
And EEC\_DTEMBA >= 'Conteúdo da pergunta Data de da *wizard* de geração do **SPED Fiscal**'  
And EEC\_DTEMBA <= 'Conteúdo da pergunta Data até da *wizard* de geração do **SPED Fiscal**'  
   
Se MV\_EEC0001 <> 1:  
Select EEC.R\_E\_C\_N\_O\_ as EEC\_RECNO  
From EECxxx EEC  
INNER JOIN EXLxxx EXL  
     On EXL.EXL\_PREEMB = EEC.EEC\_PREEMB  
     Where EEC.D\_E\_L\_E\_T\_ <> '\*' And EXL.D\_E\_L\_E\_T\_ <> '\*'  
     And EEC.EEC\_FILIAL = 'Código da sua filial' And EXL.EXL\_FILIAL = 'Código da sua filial'  
     And  (EEC.EEC\_PREEMB In (SELECT DISTINCT EE9\_PREEMB FROM EE9xxx  
     Where D\_E\_L\_E\_T\_ <> '\*'  
     And EE9\_FILIAL = 'Código da sua filial'   
     And EE9\_DTAVRB >= 'Conteúdo da pergunta Data de da *wizard* de geração do **SPED Fiscal**'  
     And EE9\_DTAVRB <= 'Conteúdo da pergunta Data até da *wizard* de geração do **SPED Fiscal**'  
     --O trecho abaixo só é processado se o campo EXL\_AVRBDS estiver preenchido  
     OR EEC.EEC\_PREEMB In (SELECT DISTINCT EXL\_PREEMB  
     FROM EXLxxx           
     Where D\_E\_L\_E\_T\_ <> '\*'  
     And EXL\_FILIAL = 'Código da sua filial'  
     And EXL\_AVRBDS <> ' '  
     And EXL\_AVRBDS >= 'Conteúdo da pergunta Data de da *wizard* de geração do **SPED Fiscal**'  
     And EXL\_AVRBDS <= 'Conteúdo da pergunta Data até da *wizard* de geração do **SPED Fiscal**'   
   
Em cima deste filtro o sistema busca as informações nas tabelas **EXL, EE9** e **EEM** para gerar as tabelas temporárias que irão gravar os registros **1100, 1105** e **1110**.
