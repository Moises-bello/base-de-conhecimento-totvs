---
content_hash: 89a86d8eccbc712f3945f181384b08db7406fc578077cdc5aba36a5acf913dda
fetched_at: '2026-06-29T00:10:02.550185+00:00'
page_id: '452718954'
product: rm
source: tdn-rm
title: Dados Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718954
version: 3
---

Esta pasta têm informações para possibilitar a contabilidade da movimentação e dos encargos da folha de pagamento.  
As informações desta pasta serão utilizadas na contabilização se o parâmetro "Utiliza cálculo por centro de custo" no parametrizador estiver desmarcado.  
   
A Integração Contábil é um agrupador de seções utilizado para contabilização, chamada de Contabilização por seção.   
   
Deve ser utilizado quando os agrupamentos exigidos pela contabilidade se aplicarem a todos os funcionários da seção. Não é necessário criar um código para cada seção. Várias seções podem estar associadas a um mesmo código de integração contábil da seção, minimizando ainda mais o trabalho posteriormente ao montar o plano de contas. O cadastro prévio dos códigos das integrações contábeis é feito na tabela dinâmica CODINTCONT no Cadastro de Tabelas Dinâmicas.  
   
Esta integração só será realizada se os campos integração contábil para conta contábil estiverem marcados no Cadastro de Eventos na pasta Dados Contábeis e/ou no Cadastro de Encargos na pasta Dados Contábeis.  
   
**Observação:**  
Os Códigos de integração contábil da seção devem ser criados de acordo com o nível de detalhamento que a contabilidade exige. Uma vez criado, deve-se atribuir a cada seção o seu código.  
   
A Integração Gerencial é um agrupador de seções utilizado para contabilização, chamada de Contabilização por seção, porém, voltado para a visão gerencial. Deve ser utilizado em casos onde a empresa necessita contabilizar por seção e faz contabilização separada entre contábil e gerencial.  
   
A utilização é idêntica à integração contábil acima.  
   
O cadastro prévio dos códigos das integrações gerenciais é feito na tabela dinâmica CODINTGER no Cadastro de Tabelas Dinâmicas.  
Esta integração só será realizada se os campos integração contábil para conta gerencial estiverem marcados no Cadastro de Eventos na pasta Dados Contábeis e/ou no Cadastro de Encargos na pasta Dados Contábeis.  
   
Nas empresas com mais de uma filial e o processamento de dados centralizado, a contabilização precisa separar os eventos e encargos de cada uma. Para isto, na seção é informado em qual filial serão contabilizados os valores referentes a esta seção. O cadastro prévio das filiais é feito no Cadastro de Filiais.  
   
Em casos onde os valores são debitados em uma filial e creditadas em outra é utilizada a filial contábil do plano de contas (veja na Contabilização os Agrupamentos de Contas Contábeis (Folha de Pagamento) ou Agrupamento de Contas Gerenciais (Folha de Pagamento)).  
   
No momento da contabilização o sistema verifica no Agrupamento de Contas se existe uma filial contábil atribuída e a usa, caso contrário, utiliza a filial contábil atribuída aqui na seção. Portanto, a filial contábil do Agrupamento de Contas tem prioridade sobre a filial contábil da seção.  
   
**Atenção:**   
Deve-se atentar para a diferença entre filial que a seção está subordinada e a filial a qual serão contabilizados os valores desta seção, que podem ser diferentes. A primeira está na pasta Identificação e a segunda na pasta de Dados Contábeis.  
   
Os Departamentos Contábeis estão relacionados ao número informado da Filial Contábil. O cadastro prévio dos departamentos é feito no Cadastro de Departamentos.  
   
Caso exista informação no Departamento Contábil da Seção e no Departamento do Agrupamento de Contas Contábeis (Folha de Pagamento) ou Agrupamento de Contas Gerenciais (Folha de Pagamento) da Contabilização, o sistema dará prioridade à informação do campo Departamento do Agrupamento de Contas ignorando a informação do campo Departamento Contábil informado na seção.   
   
Caso o campo Departamento no Agrupamento de Contas não tenha informação, o sistema buscará a informação do Departamento Contábil da seção.  
   
Algumas empresas usam, além das contas contábeis, os centros de custos para apurarem suas contas. Para estas empresas é necessário repassar para a contabilidade o número do centro de custo das despesas com a folha de pagamento, principalmente quando a contabilidade exige que sejam distribuídos os eventos ou grupos de funcionários em centros de custo separados.  
   
Esta é uma das formas a qual o centro de custo pode ser repassado para contabilidade, as outras são: No Agrupamento de Contas ou na contabilização por centro de custo. O cadastro prévio dos centros de custos é feito nos Cadastros de Centros de Custos (Folha de Pagamento).  
   
Da mesma forma que no campo integração contábil, a condição para usar este o número do centro de custo é que o centro de custo apontado aqui tem que se aplicar a todos os funcionários desta seção.   
   
Nos Cadastros do Agrupamento de Contas Contábeis (Folha de Pagamento) ou Agrupamento de Contas Gerenciais (Folha de Pagamento) na Contabilização, também tem um campo número de centro de custo contábil que tem prioridade sobre o centro de custo contábil da seção.  
   
Os campos Capital Social da Empresa e Capital Social do Estabelecimento serão utilizados para cálculo da GRCSU – Guia de Recolhimento de Contribuição Social Urbana.
