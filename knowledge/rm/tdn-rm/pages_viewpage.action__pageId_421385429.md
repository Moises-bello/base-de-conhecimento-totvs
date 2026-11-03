---
content_hash: 65138e6592c46d7c179b1fd06c0bdb3340ed541cc1e4923d4df23cd46ed21f9a
fetched_at: '2026-06-29T00:09:15.627033+00:00'
page_id: '421385429'
product: rm
source: tdn-rm
title: Insumos para contratação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385429
version: 4
---

Com a finalidade de utilização apenas em contratos, o TOTVS Obras e Projetos, permite o vínculo desses insumos a outros insumos usados somente para planejamento, sem a necessidade de um detalhamento na planilha de atividades, apenas na criação do contrato.

   

Estes insumos analíticos (chamado insumos para contratação ou insumos filhos) devem ser vinculados previamente ao insumo pai (Somente Orçamento/Planejamento) no anexo de Insumos para Contratação.

**Exemplo:**

Insumo pai (Somente Orçamento/Planejamento): EPI;  
Insumos filhos (Somente Contratação): Bota, Luva e Capacete;

Os insumos filhos (Bota, Luva e Capacete), devem ser vinculados ao insumo pai (EPI) através do anexo de "Insumos para contratação", conforme imagem a seguir:

   
**Parâmetro:**  
   
Para habilitar o anexo de insumo para contratação na tela de Insumos "F8".

É necessário marcar o parâmetro "Utiliza Insumos para Contratação" em .

Após marcar o parâmetro é necessário realizar Logout/Login no sistema.

O anexo de "Insumos para contratação" é similar a aba de "Objetos do contrato" e conterá apenas a informação do código e descrição do insumo para a contratação vinculado ao insumo principal.  
   
**Validações do cadastro de insumos para contratação:**

* Com o parâmetro "Utiliza insumos para contratação" desabilitado no projeto, ao tentar abrir o anexo de insumos para contratação será apresentada mensagem informando a respeito da a não marcação do parâmetro e sua localização.
* O insumo principal pode ter vários insumos para contratação vinculados, mas um insumo de contratação pode estar vinculado a apenas um insumo principal.
* Um Insumo principal que possui vínculo no anexo "insumos para contratação", não pode ser utilizado como insumo para contratação.
* Um insumo que já foi contratado não pode possuir insumos para contratação vinculados a ele.
* Insumos do tipo "Receita", não poderão ser utilizados como insumos para contratação. Assim, ao informar que o insumo do tipo "Receita" será automaticamente desabilitado a opção de Tipo de insumos para contratação.

Para mais informações sobre a associação de insumos do tipo contratação ao contrato de insumo, .
