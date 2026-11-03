---
content_hash: 9c0b640c6f2801f6844bc2107e020e55b8918472a010e26ad4d0c6acfe0340d2
fetched_at: '2026-06-29T00:09:47.738092+00:00'
page_id: '435105057'
product: rm
source: tdn-rm
title: Imóvel - Anexo - Área do Imóvel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105057
version: 7
---

Os registros de Área do Imóvel são necessários para o caso de utilizar várias áreas para um mesmo imóvel, possibilitando o aluguel de áreas fracionadas de um mesmo imóvel para mais de Contrato de Locação. Estas áreas podem compor o total do imóvel. O cadastro de Área do Imóvel pode ser feito através de **Aluguel / Imóvel / Anexo Área do Imóvel** ou então pelo menu **Aluguel / Cadastros / Área do Imóvel**.  Os campos disponíveis neste cadastro são:

* **Código**: Código da Área do Imóvel;
* **Compõe saldo de área para locação:** Marcando este campo, seus valores de área irão incidir sobre o valor total de área do imóvel;
* **Data de Aquisição:** Campo usado para o usuário informar qual a data que a área foi incorporada ao imóvel que ela se encontra. Este campo é editável, não sendo obrigatório;
* **Código do Imóvel:** Código do imóvel vinculado à área;
* **Código do tipo da área:** Código do tipo da área, este cadastro pode ser feito em **Aluguel / Cadastros / Tipo Área do Imóvel;**
* **Código da localização da área:** Código da Localização da Área, este cadastro pode ser feito em **Aluguel / Cadastros / Localização da Área;**
* **Descrição:** Descrição da Área do Imóvel;
* **M² Total**: Usuário deve informar a quantidade dos metros quadrados da área;
* **Valor M²**: Usuário pode informar o valor monetário do metro quadrado. Caso os campos M² Total e Valor Total estiverem preenchidos, este campo é preenchido automaticamente com o Valor monetário de Valor Total dividido pelo M² Total .
* **Valor Total:**Usuário pode informar o valor monetário total da área. Caso os campos M² Total e Valor M² estiverem preenchido, este campo é preenchido automaticamente com o Valor monetário de M² Total multiplicado pelo Valor M².
* **M² Locado Total do Imóvel**: Campo preenchido automaticamente com o somatório dos valores informados no campo "M² Locado" das áreas vinculadas a Contratos de Locação efetivados.
* **M² Disponível**: Campo preenchido automaticamente com o resultado da operação: (M² Total do imóvel - M² Locado total do imóvel).
* **M² Reservado**: Campo preenchido automaticamente que traz o somatório das áreas de um determinado imóvel vinculado a um Contrato de Locação com status de Em Preparação.
* **Centro de Custo**: Usuário pode informar o centro de custo da área. Caso informado, o processo de geração de rateio para o contrato de locação irá considerar este centro de custo.

**Observação:**

* Áreas não locadas ou não reservadas de um imóvel podem ter sua metragem alterada livremente, independente de outra área do mesmo imóvel estar locada/reservada.
* Áreas locadas ou reservadas podem ter sua metragem alterada desde que esta alteração não seja para um valor menor do que a metragem locada/reservada.
* É possível definir o número de casas decimais que serão consideradas para o campo Valor do m², que pode ser definido na tela do Parametrizador, conforme imagem abaixo (esta precisão irá impactar no calculo do valor do imóvel e consequentemente impactará o reajuste do contrato de aluguel):

Informações Complementares

---
