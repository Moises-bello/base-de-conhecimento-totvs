---
content_hash: 0b03e31f67998534cd1e19b0eb197ae8959124932e7002bfa78342355a030000
fetched_at: '2026-06-29T00:10:37.076260+00:00'
page_id: '534806714'
product: rm
source: tdn-rm
title: Subapuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=534806714
version: 22
---

Anexo do Período de Apuração em que se insere as sub-apurações, na forma como definido em legislação.   
Este Anexo possui as seguintes informações:

#### **Validações realizadas para o Encerramento**

1. O Período de Apuração (pai) deve estar com status Aberto;
2. O período de Subapuração imediatamente anterior de mesmo Identificador deve estar encerrado;
3. O Lote Fiscal (caso seja utilizado) deve estar Aberto.

#### **Seleção dos Lançamentos Fiscais**

No Encerramento serão selecionados Lançamentos Fiscais de Entrada e Saída, que atendam aos seguintes critérios:

1. Possuam Ajuste vinculado ao Lançamento ou ao Item;
2. Pertençam à Coligada\Filial do Período de Apuração;
3. Cuja **DATALF** esteja dentro do período da Subapuração;
4. Com Status Normal ou Estornado;
5. Associados a CFOP Fiscal;
6. Cujo Lote Fiscal esteja Liberado (caso utilize Lote Fiscal);

#### **Identificador da Subapuração** (1900\_2) - O Manual do SPED define previamente os códigos válidos:

* 3 – APURAÇÃO 1;
* 4 – APURAÇÃO 2;
* 5 – APURAÇÃO 3;
* 6 – APURAÇÃO 4;
* 7 – APURAÇÃO 5;
* 8 – APURAÇÃO 6

Esses códigos definem quais os Códigos de Ajustes do C197/D197 devem ser considerados na apuração.   
Por exemplo: para a sub apuração de código “**3**” devem ser considerados os Códigos de Ajustes cujo 4º dígito do código seja “**3**”.

**Descrição** (1900\_3) - Este campo deve ser preenchido conforme definido pelas legislações dos Fiscos Estaduais.   
De acordo com o Manual, deve ser descrita a norma legal que exige a apuração em separado. 

**Período da Subapuração** (Data Inicial e Data Final) (1910\_2/3)- O período da sub apuração não necessariamente acompanha o período de apuração do ICMS/ICMS ST.   
Mas, aquela deve estar contida dentro desta.   
Além disso, não devem existir lacunas ou sobreposições de datas, comparadas ao período do arquivo informado no Registro 0000 do SPED Fiscal que hoje recebe o intervalo do período de apuração do ICMS.  
Deste modo, para Sub Apurações com mesmo identificador de sub apuração, não será possível inserir períodos de data inicio e fim que tenham interseção.

**Gerar no SPED** - Flag para identificar se a subapuração deve ser gerada no arquivo do SPED Fiscal ou não.

**Considerar somente as Entradas referenciadas em notas de Saída**- Este flag vai identificar se, durante o encerramento, o sistema deve considerar todas as Notas Fiscais de Entradas do período (varejista) ou somente as entradas que estejam associadas a Notas Fiscais de Saídas (não varejista). Não afeta a seleção das Notas Fiscais de Saída.

**Status** - Este campo deve ser alterado somente pelo processo de **abertura** e  e deve conter as opções “**Aberto**” e "**Encerrado"**.

Este Anexo possibilitará a geração dos Registros 1900, 1910 e 1920 do Sped Fiscal.

 **Pasta "Valores"**

Os valores serão calculados ao executar o processo de encerramento seguindo regras para o cálculo do valor apurado. Abaixo o link com todo o detalhamento.

---
