---
content_hash: edaaf992ca0db4b92a1661664fa9ec2809ac9d9b40265f3395dbbee121f030cc
fetched_at: '2026-06-29T00:09:12.803847+00:00'
page_id: '417700533'
product: rm
source: tdn-rm
title: Unidade Clínica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=417700533
version: 1
---

**Unidade Clínica**

---

Esta tela tem a finalidade de cadastrar as unidades de internações, já cadastradas no sistema do hospital. Permite você incluir, editar ou excluir o cadastro. São editáveis os campos, unidade clínica, taxa geral e nº de leitos. Os códigos das unidades clínicas não são editáveis, são gerados automaticamente ao incluir uma nova unidade clínica.   
Para as unidades clinica já cadastradas na base o código da unidade será replicado no campo código cliente podendo ser editado caso não corresponda ao código da unidade clinica da base a ser importada.  
Ao incluir uma nova unidade clinica não será replicado o código da unidade, neste caso devera informar o código correspondente a esta unidade da base a ser importada.  
**Observações**  
Unidades Clínicas em que o número de admissões será computado de forma integral no número total de pacientes da taxa global da instituição (devem-se considerar todas as unidades de internação). Deve-se também considerar aqui o cadastro de unidades de Day Surgery, onde vemos número crescente de procedimentos cirúrgicos NHSN ou não, serem realizados em pacientes que ficarão poucas horas em enfermarias ou apartamentos contíguos a estes blocos, recebendo alta no mesmo dia. Se por um lado estes pacientes não preenchem critérios de paciente NHSN pelo fato de receberem alta no mesmo dia, julgamos que devemos computá-los no cálculo do denominador da taxa global devido o fato de suas infecções cirúrgicas (procedimentos NHSN ou não) habitualmente serem considerados nos numeradores da taxa global.   
Aplicável às unidades de terapia intensiva (área crítica), onde a maioria dos pacientes recebe alta do hospital em outras unidades clínicas após a alta do CTI. Estes pacientes já serão computados pelo sistema na unidade clínica onde internou. Será considerado para cálculo do denominador da taxa global apenas os pacientes das áreas críticas que obituam nestas unidades, recebem alta diretamente para o domicílio (comum em unidades neonatais) ou que são transferidos para CTI´s de outras instituições. Neste grupo o número de pacientes que aparece na tabela do relatório para cada uma das unidades críticas não são somados na íntegra para composição do denominador da taxa global da instituição. Apenas uma pequena parcela destes (não visível, entretanto, calculado e somado pelo sistema) que foram internados na área crítica diretamente ao internar no hospital são somados ao total do denominador em que perceberão uma diferença no total.   
Refere-se apenas ao Berçário de Recém Nascidos Normais, nível I, pois na grande maioria das instituições estes neonatos não recebem registro próprio, portanto, não são importados para a base de dados do RM Janus. Neste caso o cadastro do denominador das taxas de Berçário, quer seja de número de RN´s ou de pacientes/dia destas unidades deverão ser cadastrados obrigatoriamente no menu cadastros/população/admissões. A categorização do Berçário como "C" fará com que o software busque o denominador nesta tabela de "População". Obviamente, todos estes RN´s serão computados para o denominador da taxa global. Esta categoria também pode ser usada para outras unidades em que o paciente não interna, mas que desejam acompanhar sua taxa, exemplo, Hemodiálise, etc. Devem seguir o mesmo cadastro do Berçário.   
   
Última atualização – Novembro de 2010
