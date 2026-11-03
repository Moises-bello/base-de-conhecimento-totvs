---
content_hash: 987636b798625716597c0439a3b012204e1580a731bbbaf0aa97d922f4c833e4
fetched_at: '2026-06-29T00:09:27.240842+00:00'
page_id: '423938458'
product: rm
source: tdn-rm
title: Identificação - Partida
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938458
version: 11
---

***Atenção**!*   
   
Esta funcionalidade só está disponível para as bases já migradas para o Novo Modelo do BackOffice.  
   
Esta é a janela onde os dados referentes a cada Partida que compõe o Lançamento deverão ser preenchidos.

As Partidas representam os Débitos e os Créditos do Lançamento, podendo então em uma mesma Partida ser lançado o Débito e também Crédito ou então, incluir Partidas separadas para o Débito e para o Crédito, lembrando que, independente da forma de inclusão das Partidas, o valor de Débito deve sempre ser igual ao valor de Crédito.   
Alguns campos desta janela são de preenchimento obrigatório e estarão em negrito.

Na **Inclusão** de partidas alguns campos já poderão vir preenchidos automaticamente conforme Fixação de Campos definida em Utilitários / Preferência do Usuário.  
A exibição ou não de alguns campos desta tela assim como a forma de utilização de outros está diretamente ligada à maneira como o sistema está parametrizado, veja em Ambiente / Parâmetros / TOTVS Gestão Contábil.

Na **Edição** de partidas alguns campos ficarão desabilitados, ou seja, suas informações não poderão ser alteradas. Isto se deve a vários motivos, por exemplo:

* Dependendo da parametrização feita no sistema, não será permitido alterar a Filial. Veja o parâmetro "Permite diferenças entre filiais".
* Se o lançamento tiver sua origem em outros aplicativos, não será permitido alterar a descrição e data do lançamento, o valor e 2º valor. Se uma partida veio da origem somente com o débito, não será permitido adicionar uma nova conta no crédito e vice-versa. Se uma partida veio da origem com o débito e com o crédito preenchidos, não será permitido excluir uma das contas deixando a partida somente com o débito ou com o crédito. (Estas regras valem para os aplicativos que já migraram para o novo modelo de BackOffice - nova plataforma .NET )
* Se o lançamento tiver sua origem em outros aplicativos, e a conta contábil for alterada ou o rateio for incluído/alterado/excluído, esta alteração refletirá na origem. (Estas regras valem para os aplicativos que já migraram para o novo modelo de BackOffice - nova plataforma .NET )
* Não será permitido excluir/incluir lançamentos em lotes que tiverem sua origem em outros aplicativos da mesma forma como não será permitido excluir/incluir partidas em lançamentos que tiverem sua origem em outros aplicativos, caso uma destas operações seja necessária a mesma deverá ser feita no aplicativo de origem respeitando as regras de integração com a contabilidade. (Estas regras valem para os aplicativos que já migraram para o novo modelo de BackOffice - nova plataforma .NET )

**Observações**

* Se os lançamentos ainda estiverem em Lote, a exclusão somente poderá ser feita na origem refletindo assim, no Lote de lançamentos. Se os lançamentos já estiverem no Lote Zero, a exclusão somente poderá ser feita através de estorno realizado na origem, onde serão incluídos lançamentos contrários aos originais.
* Se o lançamento tiver sua origem em outros aplicativos, e for um lançamento de estorno ou estornado, o mesmo ficará somente leitura, ou seja, desabilitado para alterações.
* Se as partidas de um lançamento tiverem sido agrupadas pelo processo de Agrupamento, o mesmo ficará somente leitura, ou seja, desabilitado para alterações.
* Se o lançamento estiver bloqueado para outro usuário, todos os seus campos ficarão desabilitados. (Na inclusão/edição de um lançamento, enquanto a soma dos Débitos não for igual à soma dos Créditos este lançamento ficará bloqueado com o usuário que o estiver incluindo/editando. Mesmo que não haja diferença entre débito e crédito o lançamento permanecerá bloqueado com o usuário que o está editando e só será desbloqueado quando a tela for fechada)
* Não é permitido efetuar quaisquer manutenções na partida caso sua data (que é a data de seu lançamento) seja menor que a data de conciliação de uma de suas contas contábeis. Acessar [Conciliação](https://tdn.totvs.com/pages/viewpage.action?pageId=686485866) para maiores detalhes sobre Conciliar/Desconciliar, Concluir conciliação, Conta conciliada, Data de conciliação, etc.

**Atenção!  
Eliminação:**Em operações intercompany só é permitido utilizar uma Conta Contábil por Partida.

**Atenção para as regras à seguir!**  
Manutenções em Lançamentos provenientes de outros aplicativos e que foram gerados **antes** da conversão para o novo modelo de BackOffice ou provenientes de outros aplicativos que ainda não converteram para o novo modelo de BackOffice:  
   
1- **Não** permite alterar Data e Descrição.   
2- **Não** permite incluir Partidas.   
3- Permite alterar Valor.   
4- Permite acrescentar na partida, uma conta de débito ou de crédito.   
5- Permite remover na partida, uma das contas (conta de débito ou conta de crédito).   
6- Permite excluir uma partida.   
7- Permite incluir e excluir um lançamento.   
8- Permite excluir o lote N (lote antes de ser integrado ao lote zero).   
9- No caso específico de lançamentos originados da Folha de Pagamento, também será possível incluir partidas.   
10-Os lançamentos originados do módulo Fiscal e do módulo de Estoque, Compras e Faturamento mesmo sendo originados no antigo modelo contábil receberão o mesmo tratamento de lançamentos originados no Novo Modelo, onde as alterações deverão ser feitas na origem.   
11-Os Parâmetros do sistema que permitem ou barram alteração/exclusão de lançamento do Fluxus ou Labore  somente serão respeitados para lançamentos originados antes do novo modelo de BackOffice.
