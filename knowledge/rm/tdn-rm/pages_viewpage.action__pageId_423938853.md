---
content_hash: 74ef5830efdad5d553cd8717605ecb19572abc94e090d57d10967068347bb0c6
fetched_at: '2026-06-29T00:09:29.252993+00:00'
page_id: '423938853'
product: rm
source: tdn-rm
title: Registros Bloco K210 e K215 (SPED Fiscal)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938853
version: 2
---

Alguns segmentos apresentam a figura da "desmontagem" e esse processo era tratado anteriormente no Bloco K (Controle da Produção e do Estoque) como movimentação interna de mercadorias, porém agora as empresas podem tratar como uma "Industrialização", ainda que caracterizada apenas como Ordem de Serviço (OS).  
 Essas informações foram divididas em dois registros:

1. **K210** – Desmontagem de Mercadorias – Item de Origem: Esse registro trata de informações sobre as mercadorias, que serão destinadas ao desmonte, informando a data da retirada do estoque e a quantidade.
2. **K215** – Desmontagem de Mercadorias – Item de Destino: Nesse registro o enfoque são as informações sobre as mercadorias que serão originadas com o desmonte, devendo ser elencado nesse registro todos os códigos e quantidades que resultaram desse desmonte.

No TOTVS Gestão de Estoque, Compras e Faturamento o processo de desmontagem é feito a partir da cópia por referência do movimento de baixa da estrutura de origem, que possibilita a criação automática do movimento de entrada dos itens de destino, onde se cria o vínculo entre estes movimentos.   
Para a desmontagem do item de origem, que deve conter estrutura ou semiacabado ou ambos, pode ser usado qualquer movimento de baixa do tipo 2.2.XX e deve retirar as estruturas do estoque da empresa.   
Como se trata de uma movimentação interna, é necessário criar o movimento de entrada do tipo 1.2.XX que utilize o motivo de cópia referência criado para esse processo, que é 29 - Desmontagem de Mercadorias.   
Assim o sistema conseguirá em um determinado período localizar quais os movimentos de entrada gerado por referência 29 e enviar seus dados para o Registro K215 no SPED.   
Para o registro do K210 no SPED serão enviados os dados da baixa que originaram as entradas.  
No assistente de cópia por referência o motivo de cópia referência 29 permite que seja efetuada a cópia de apenas um movimento por vez, mas um mesmo movimento pode conter várias estruturas. Também verifica se os itens do movimento de origem são todos estruturas.   
Se sim, ele permite a continuação do processo de cópia, Se não, ele barra a continuação do processo e se houver itens com e sem estrutura, copia só os que são estruturas.   
Para gerar o movimento de entrada, deve-se explodir a estrutura e visualizar seus componentes, pois são eles que serão levados para o movimento.   
O sistema permite explodir todas ou selecionar quais devem ser explodidas.   
No momento de explodir, o sistema exibe uma mensagem questionando se a explosão da estrutura deve ser até o último nível, ou seja, se a estrutura houver como componente semiacabado, que também é uma estrutura, deve ser explodida ou não.   
Caso o usuário escolha a opção Sim, a estrutura é explodida e se houver componente com estrutura (semiacabado) também será explodido, desde que o mesmo não seja tratados como matéria prima na composição.   
Se o componente com estrutura (semiacabado) for tratado como matéria prima, mesmo escolhendo sim, ele não será explodido.   
Essa explosão poderá ser feita no movimento. Caso o usuário escolha a opção Não, independente se na estrutura há componente com estrutura (semiacabado) tratado ou não como matéria prima, serão explodidos só até o nível de matéria prima, ou seja, o semiacabado que é componente não será explodido, sendo possível esse ser explodido no movimento.  
Ainda no assistente, o item vindo da baixa (estrutura) não pode ser excluído e sua quantidade não pode ser alterada.   
Após a explosão dos componentes, os mesmo podem ser excluídos, porém a quantidade não é exibida, não sendo possível alterá-la e nem adicionar outros componentes. As alterações podem ser feitas no movimento.   
Assim ao avançar o assistente o movimento será gerado. Após terem sido gravadas todas as movimentações internas de desmontagem do mês, o sistema estará apto a gerar os Registros K 210 e K 215 do Bloco K do SPED Fiscal no TOTVS Gestão Fiscal.

Informações Adicionais

* [Bloco K - Registros K210 e K215](http://tdn.totvs.com/display/LRM/TVZXFP+DT+Bloco+K+-+Registros++K210+e+K215)
