---
content_hash: ae65f3f5f7cf78ad1bd0fde93554f06cdda1a488c176661b03b4a08b87267923
fetched_at: '2026-06-29T00:09:35.981861+00:00'
page_id: '425459453'
product: rm
source: tdn-rm
title: Cancelamento do Contrato X Contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459453
version: 4
---

---

Quando um contrato é **Cancelado**, o sistema não permite que mais nenhuma ação seja feita para o mesmo, porém mantem para efeito de histórico todas as informações contidas no contrato até o momento. Ao cancelar um contrato, se o mesmo já tiver sido contabilizado, os lançamentos contábeis referentes às contabilizações já realizadas não serão excluídos. O sistema, porém, fará ajustes entre os valores contratados e não realizados.

A forma como os ajustes serão realizados irá variar conforme o modelo definido na parametrização do sistema para a realização da contabilização por competência do contrato educacional.

Utilizando o mesmo cenário, vejam a seguir como serão ajustados os valores contratados e não realizados nos dois modelos de contabilização:

**1 - Primeiro Modelo de Contabilização:**Onde **somente** a primeira opção 'Utiliza contabilização por competência', presente nos parâmetros do sistema, deve estar marcada.

**Vamos supor o exemplo abaixo:**  
 -Competência - Mês/Ano Inicial: 01/2015  
 -Competência - Mês/Ano Final  : 12/2015  
 -Data do Contrato: 03/03/2015  
 -Valor total dos serviços do contrato a ser contabilizado: 12.000,00  
 -Valor de cada competência a ser contabilizada: 1.200,00  
 -Contabilizações já realizadas para o contrato até a competência 04/2015:

**Evento contábil utilizado para contabilizar o 'Contrato':**  
 D – 1.1.2.04.01.001 - Mensalidades a Receber  
 C – 2.1.7.01.01.001 - Receitas de Graduação

**Evento contábil utilizado para contabilização 'Mensal':**  
 D – 2.1.7.01.01.001 - Receitas de Graduação  
 C – 3.1.1.01.01.001 - Receitas de Graduação

Lançamento referente à contabilização do valor do contrato:  
 D – 1.1.2.04.01.001 – 12.000,00  
 C – 2.1.7.01.01.001 – 12.000,00

Lançamento referente à contabilização da primeira competência do contrato (mês 03/2015):  
 D – 2.1.7.01.01.001 – 1.200,00   
 C – 3.1.1.01.01.001 – 1.200,00

Lançamento referente à contabilização da segunda competência do contrato (mês 04/2015):  
 D – 2.1.7.01.01.001 – 1.200,00   
 C – 3.1.1.01.01.001 – 1.200,00

- O contrato foi Cancelado em 30/04/2015.   
 - Os lançamentos já incluídos não serão excluídos.  
 - O sistema fará o cálculo dos valores que já foram apropriados ou realizados até o momento = **2.400,00** (1.200,00 referente à competência 03/2015 + 1.200,00 referente à competência 04/2015).

**1 - Se os lançamentos ainda estiverem no Lote N:**  
 Os lançamentos referentes às contabilizações já realizadas não serão excluídos, porem o sistema irá alterar o lançamento existente referente à contabilização do valor original contrato, alterando o ***valor*** deste lançamento para o valor total já apropriado ou realizado até o momento, conforme cálculo demonstrado anteriormente (2.400,00), correspondendo assim aos valores já lançados para as competências mensais:

- O lançamento referente à contabilização do valor original do contrato (12.000,00), será alterado para o novo valor = 2.400,00, conforme demonstrado anteriormente:  
 D – 1.1.2.04.01.001 – 2.400,00  
 C – 2.1.7.01.01.001 – 2.400,00

- Os lançamentos referentes às contabilizações mensais serão mantidos sem alterações.  
 - Finalmente o sistema fará o *cancelamento* propriamente dito do contrato.  
    
 **2 - Se os lançamentos já tiverem sido integrados ao lote oficial da contabilidade – Lote 0:**  
 Como regra, os lançamentos já integrados ao **lote 0 (zero)** não podem sofrer alterações, então nestes casos, o sistema fará o *estorno* com o intuito de *'anular ou cancelar'* o lançamento referente à contabilização do valor original do contrato da seguinte forma: O lançamento original, que está no Lote 0 (zero), não será excluído, mas terá o status alterado para '**I** = Incorreto'. Será incluído no lote criado especificamente para receber os estornos, o respectivo lançamento de estorno, no mesmo valor, para *'anular'* o efeito do lançamento anterior e receberá o status '**E** = Estorno'. O evento utilizado para realização do estorno será o evento de 'Contrato', havendo simplesmente a inversão das contas contábeis. Fará também o cálculo dos valores que já foram apropriados ou realizados até o momento e, com este valor, incluirá então, novo lançamento para a contabilização do contrato, correspondendo assim aos valores já lançados para as competências mensais. Este lançamento receberá o status **'C** = Correto' e será incluído no lote parametrizado para inclusão da contabilização:

- Lançamento referente à contabilização do valor original do contrato já integrado ao lote zero: terá o status alterado para '**I**'.

- Inclusão do lançamento de estorno referente à contabilização do valor original do contrato no lote de Estorno com status = '**E**':  
 D – 2.1.7.01.01.001 – 12.000,00  
 C – 1.1.2.04.01.001 – 12.000,00

- Inclusão do lançamento no lote N referente à contabilização do valor realizado do contrato 2.400,00 com status = '**C**', conforme demonstrado anteriormente:  
D – 1.1.2.04.01.001 – 2.400,00  
C – 2.1.7.01.01.001 – 2.400,00

-Os lançamentos referentes às contabilizações mensais serão mantidos sem alterações.  
- Finalmente o sistema fará o *cancelamento* propriamente dito do contrato.

**2 - Segundo Modelo de Contabilização:**  
Onde as **duas** opções 'Utiliza contabilização por competência' **e também** 'Registra separadamente contabilizações de cancelamento e aumento', presentes na parametrização do sistema, devem estar marcadas.

**Vamos supor o exemplo abaixo:**  
 - Competência - Mês/Ano Inicial: 01/2015  
 - Competência - Mês/Ano Final  : 12/2015  
 - Data do Contrato: 03/03/2015  
 - Valor total dos serviços do contrato a ser contabilizado: 12.000,00  
 - Valor de cada competência a ser contabilizada: 1.200,00  
 - Contabilizações já realizadas para o contrato até a competência 04/2015:

**Evento contábil utilizado para contabilizar o 'Contrato':**  
 D – 1.1.2.04.01.001 - Mensalidades a Receber  
 C – 2.1.7.01.01.001 - Receitas de Graduação

**Evento contábil utilizado para contabilização 'Mensal':**  
 D – 2.1.7.01.01.001 - Receitas de Graduação  
 C – 3.1.1.01.01.001 - Receitas de Graduação

Lançamento referente à contabilização do valor do contrato:  
 D – 1.1.2.04.01.001 – 12.000,00  
 C – 2.1.7.01.01.001 – 12.000,00

Lançamento referente à contabilização da primeira competência do contrato (mês 03/2015):  
 D – 2.1.7.01.01.001 – 1.200,00   
 C – 3.1.1.01.01.001 – 1.200,00

Lançamento referente à contabilização da segunda competência do contrato (mês 04/2015):  
 D – 2.1.7.01.01.001 – 1.200,00   
 C – 3.1.1.01.01.001 – 1.200,00

- O contrato foi Cancelado em 30/04/2015.   
 - Os lançamentos já incluídos não serão excluídos.  
 - O sistema fará o cálculo dos valores que já foram apropriados ou realizados até o momento = **2.400,00** (1.200,00 referente à competência 03/2015 + 1.200,00 referente à competência 04/2015).

Quando a empresa utiliza o **segundo** modelo de contabilização, o sistema **não** realiza estorno dos lançamentos já contabilizados, mas sim, utiliza eventos contábeis específicos para registrar os novos fatos e**,** independentemente se os lançamentos ainda estiverem no **Lote N** ou se já tiverem sido integrados ao lote oficial da contabilidade – **Lote 0**, o procedimento será o mesmo: o sistema fará o cálculo dos valores que já foram apropriados ou realizados até o momento, (2.400,00) conforme demonstrado anteriormente, e fará um lançamento para cancelar os valores que não serão realizados devido ao cancelamento do contrato, no valor de **9.600,00** (12.000,00 – 2.400,00 = 9.600,00). Para isto irá utilizar o evento contábil criado previamente, específico para registrar Cancelamentos:

**Evento contábil utilizado para contabilizar 'Cancelamento do Contrato':**  
 D – 2.1.7.01.03.001 – Cancelamento de Matrícula  
 C – 1.1.2.04.01.001 – Mensalidades a Receber

- Inclusão do lançamento para Cancelamento dos valores não realizados do contrato, utilizando o evento para cancelamento:  
 D – 2.1.7.01.03.001 – 9.600,00  
 C – 1.1.2.04.01.001 – 9.600,00

- Os lançamentos já existentes serão mantidos sem alterações.  
 - Finalmente o sistema fará o *cancelamento* propriamente dito do contrato.
