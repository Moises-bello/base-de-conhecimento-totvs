---
content_hash: cf09fd9e795bd9c84bdd4b0da7740b75953694b405b78a228af719afdc078d9a
fetched_at: '2026-06-29T00:05:59.331123+00:00'
page_id: '189310653'
product: rm
source: tdn-rm
title: 'RMCTB000010_Perguntas e Respostas: SPED (ECD e FCONT)'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=189310653
version: 15
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | TOTVS Gestão Contábil - Versão 11.82 e posteriores |
| **Processo** | : | Workshop realizado no dia 28/05/2015 |
| **Data da publicação** | : | 05/06/2015 |

**Perguntas e respostas**

1. As Entidades imunes/isentas este ano serão as primeiras em obrigatoriedade do SPED ECD. Para facilitar o processo, elaboramos um passo a passo básico de configurações e informações que deverão ser realizadas no sistema. [Clique](http://tdn.totvs.com/pages/releaseview.action?pageId=61931762) para conhecê-las.
2. Erro: "O valor informado nas contas de maior detalhamento do registro da DRE não corresponde à soma dos valores informados nos registros de Saldos das Contas de Resultado antes da Apuração na mesma data."   
   Solução: Verifique se todas as classificações da conta contábil foram informadas corretamente e analise a associação do plano referencial X Contábil.
3. É possível imprimir o balanço em um nível mais sintético ou o relatório só é emitido analiticamente?  
   Resposta: No momento de gerar o arquivo, na tela das demonstrações informe qual o grau deverá ser enviado para o balanço Patrimonial.
4. Como ajustar a advertência: Um lançamento pode ter vários registros a débito e vários a crédito somente quando relativos ao mesmo fato contábil (Resolução CFC 1299/2010)?  
   Resposta: Verifique se a situação está correta. [Clique](http://tdn.totvs.com/pages/releaseview.action?pageId=187534249) e saiba mais.
5. O processo de atualização dos participantes, faz o cadastro do participante automaticamente?  
   Resposta: É necessário cadastras no TOTVS Gestão Contábil os Participantes e seus relacionamentos. Dependendo de onde vem a informação o campo Participante no lançamento poderá vim preenchido. [Clique](http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.participantes.aspx) e saiba mais.
6. Qual SPED cujo prazo foi prorrogado para Setembro/2015?  
   Resposta: A ECF (Escrituração Contábil Fiscal).
7. Como gerar FCONT?  
   Resposta: [Clique](http://tdn.totvs.com/display/public/rm/SPED+FCONT) e conheça todos os documentos referentes ao FCONT.
8. Pode usar o mesmo Plano Referencial tanto para SPED quanto para FCONT?  
   Resposta: Não. O plano referencial para o FCONT não sofreu mudanças e assim deverá usar o mesmo do ano base de 2013.
9. Esse processo todo demonstrado, só é possível fazê-lo pela interface nova MDI?  
   Resposta: Não. Pode ser feito também pelo executável (RM Saldus.exe)
10. Pode-se desprezar as demonstrações BP, DRE e DMPL do Saldus e incluí-las no J800?  
    Resposta: Não. Estas demonstrações, de acordo com o layout da RFB, possuem registros próprios e deverão ser gerados por eles.
11. Como enviar as notas explicativas no SPED?  
    Resposta: Neste caso, como não há registro especifico poderá inclui-la no J800, lembrando que o arquivo deverá ter o formato em rtf.

    
 **Assunto: SCP**

1. É necessário ter CNPJ para a SCP ou pode usar um outro código?  
   Resposta: De acordo com a informação do link <http://www.contabeis.com.br/noticias/21054/a-scp-e-a-exigencia-de-sua-inscricao-no-cnpj/> , as SCP's são obrigadas a terem inscrição no CNJP, mas sugerimos que esta obrigatoriedade seja verificada pelo departamento fiscal da empresa junto à RECEITA FEDERAL.
2. E quando existe um histórico de fechamento para cada SCP, basta informar o histórico para geração de cada filial?  
   Resposta: Pode utilizar um histórico de fechamento para cada SPC. O que deve ser reforçado é que a apuração de resultados no TOTVS Gestão Contábil, quando se trabalha com SCP,  deve ser feito por filial, assim será possível obter os valores de Lucro/Prejuízo de cada filial SCP. Portanto, orientamos que seja criada uma estrutura e para cada filial seja criada um molde de transferência de grupos contábeis. Assim será possível obter os resultados de Lucro/Prejuízo por filial.
3. Para cada SCP precisa criar DRE e DLPA?  
   Resposta: Se os fatos contábeis das demonstrações estiverem configurados com filtros genéricos específicos será necessário criar uma demonstração para cada SCP's e uma para o sócio ostensivo. Se as demonstrações estiverem configuradas buscando somente saldos ou movimentações de contas contábeis não haverá necessidade.
4. O sócio ostensivo também deve ter o parâmetro 'Filial é SCP' marcado?  
   Resposta: Não, somente a filial que for SCP.
5. Como fazer a separação das demonstrações por SCP?  
   Resposta: No TOTVS Gestão Contábil a apuração de resultados é feita por filial, portanto como cada SCP é uma filial no sistema, a apuração de resultados deverá ser feita por filial. Desta forma será possível obter os resultados separados.

  **Assunto: DMPL**

1. Como elaborar a DMPL?  
   Resposta: A DMPL - Demonstração das Mutações do Patrimônio Líquido, deve demonstrar todas as movimentações das contas do patrimônio Líquido, portanto o responsável pela montagem desta demonstração deverá emitir um relatório que demonstre toda a movimentação das contas deste grupo. O relatório mais utilizado para obter estes valores é o razão analítico. Com estas informações a demonstração será montada de acordo com a movimentação do patrimônio líquido de cada empresa. Existem vários padrões de DMPL que podem ser obtidos na internet, se desejado a TOTVS também disponibiliza templates padrões que podem auxiliar na montagem.
2. A DMPL é obrigatória?  
   Resposta: As Sociedades Anônimas S.A's e as empresas de grande porte são obrigadas a publicar suas demonstrações contábeis, dentre elas está a DMPL. Com relação ao SPED Contábil se as demonstrações DMPL ou DLPA não forem geradas, o arquivo o validador do SPED Contábil irá verificar se a data de encerramento do exercício social está dentro do período da escrituração. Caso esteja, será gerada uma advertência informando que a DLPA ou DMPL deve ser inserida no final do exercício. Portanto, o SPED Contábil considera a falta das demonstrações neste caso como advertência. Nossa orientação é que as demonstrações que são exigidas no arquivo sejam enviadas.
3. Se a instituição publicou a DMPL e a DLPA deve também informar estas duas demonstrações?  
   Resposta: O layout do SPED Contábil exige uma das duas demonstrações, não é possível enviar as duas. A DMPL é uma e já contempla a DLPA pois nela consta a conta de Lucros/Prejuízos Acumulados.
4. Existe algum modelo para criação dessas Demonstrações Contábeis?  
   Resposta: A TOTVS disponibiliza templates padrões que podem ser baixados a partir do próprio sistema, desde que seja acessado pela nova MDI(RM.exe).   
   Após acessar, clique na aba lateral superior direita denominada "TOTVS By You. Informe o nome para a pesquisa, exemplo DMPL. Clique no ícone By You (rodapé direito) para pesquisar. Paginar para localizar e fazer o download. Feito isso, promova as alterações conforme necessidade.  
     
     
     
     
   Se a aba **TOTVS By You** não estiver visível acesse o menu: **Ambiente / Parâmetros / Globais**. Localize a aba **Performance** e marque a opção **Habilitar painel de pesquisa no Fluig.**
5. Que tipo de empresa se enquadra na DMPL e DLPA?  
   Resposta: As Sociedades Anônimas S.A's e as empresas de grande porte são obrigadas a publicar suas demonstrações contábeis, dentre elas está a DMPL. Estas empresas não publicam DLPA, pois a DMPL já contempla a conta de Lucros/Prejuízos Acumulados. As demais empresas não estão obrigadas, mas podem elaborar as duas demonstrações, ficando a cargo do departamento contábil da empresa definir qual será a demonstração a ser enviada para o SPED Contábil verificando as exigências legais.
6. Em nossa demonstração virtual realizado no dia 28/05/2015, foram feitos dois processos: um para gerar DLPA para o SPED, e depois para a DMPL. Não pode fazer um processo só para as duas demonstrações?  
   Resposta: O layout do SPED Contábil exige uma demonstração ou outra. As duas não são permitidas conforme layout, pois a DMPL já contempla a DLPA.
7. Qual a diferença de Fato Contábil e Fato contábil de saldo inicial DLPA/DMPL?  
   Resposta: Atualmente no validador do SPED Contábil no caso da DLPA, o saldo inicial e final não são calculados, então é preciso configurar o fato que será considerado como saldo inicial e final para que internamente o sistema interprete os valores corretamente na demonstração contábil. Para mais detalhes, [clique aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=187534251).
8. Se eu configurar a DMPL para uma coligada posso copiar para as outras coligadas da base? (Plano de contas contábil global)  
   Resposta: Sim. Se o plano de contas for global, a estrutura da demonstração poderá ser exportada da coligada X e importada na coligada Y. Como as contas são globais a configuração dos fatos permanecerá.
9. Somente poderá vincular as demonstrações contábeis geradas na nova ferramenta de demonstrações contábeis?  
   Resposta: O balanço e a DRE podem ser geradas pela ferramenta, automaticamente pela classificação das contas ou pelo relatório interno do sistema (DRE). Já a DMPL ou DLPA só podem ser geradas a partir de estruturas criadas na ferramenta de demonstrações contábeis.
10. A utilização da demonstração de resultado é correlacionada com a geração da DMPL?  
    Resposta: Não, a DRE não está relacionada com a DMPL. A DRE também pode ser elaborada pela ferramenta de demonstrações contábeis, mas são demonstrações que são configuradas independentes.
11. Caso não exista a estrutura montada da DMPL ou DLPA no sistema, é obrigatório a entrega do SPED com a estrutura? Existe outra forma de anexar a DMPL ou DLPA direto no validador?  
    Resposta: Para que o sistema possa gerar o registro referente a DMPL/DLPA é necessário que exista uma estrutura criada na ferramenta de demonstração contábil. Sem ela não será possível gerar o registro no arquivo. O validador do SPED Contábil permite que o registro de DMPL/DLPA seja incluído direto no validador.

**Assunto: Plano Referencial**

1. Existe um plano de contas referencial novo ou é permitido utilizar do ano anterior?  
   Resposta: Para a ECD a RFB publicou novos planos referenciais. Para download [veja instruções](http://tdn.totvs.com/display/public/rm/Plano+de+Contas+Referencial+-+Layout+3.0) .
2. O plano demonstrado na capacitação virtual é da versão 11.80, serve também para a 11.82.38?  
   Resposta: O plano referencial pode ser importado a partir da versão 11.82.38 e posteriores.
3. Não estamos encontrando essa opção de importação de arquivos.  
   Resposta: Verificar se a versão é 11.82.38 ou posteriores e confira também as permissões de acesso no perfil do usuário.
4. É necessário vincular as contas paralelas novamente, uma vez que só é permitido copiar plano de contas com a mesma máscara?  
   Resposta: Sim. A RFB mudou o plano referencial e o mesmo não contempla a mesma máscara do plano anterior.
5. Se for configurado o plano de contas referencial errado, é preciso desfazer os links das contas contábeis e referenciais uma a uma, ou basta selecionar outro plano de contas referencial e fazer novos links?  
   Resposta: Deverá ser feita uma por uma. Dica: importar o plano referencial novamente e usar este para geração da rotina.
6. Sendo as máscaras de contas diferentes, é possível efetuar a cópia das associações?  
   Resposta: Não, a cópia só é realizada quando tanto o plano de Origem quanto o plano de Destino possuírem a mesma máscara, conta e descrição da conta.
7. Durante a apresentação virtual, na criação do plano de contas, não foi preenchido a máscara. Esse campo não precisa ser preenchido?  
   Resposta: Não, basta no processo marcar a flag para Não validar a máscara.
8. Trabalhamos com várias empresas que utilizam o mesmo plano de contas societário. Após o vínculo das contas em uma das empresas, vamos conseguir copiar o plano contendo as associações para as demais empresas?  
   Resposta: Sim. Deverá ser rodado o script que habilita a ECF (gerada no TOTVS Gestão Fiscal), assim,  no cadastro do plano paralelo no TOTVS Gestão Contábil, em Processos,  será habilitada a opção de Cópia entre Coligadas.
9. Se já tiver um plano de contas paralelo referencial precisa fazer algum ajuste para esse ano? Ou teremos que importar novamente?  
   Resposta: Para o ano base de 2014 o plano referencial é diferente do ano base de 2013. Para download [veja instruções.](http://tdn.totvs.com/display/public/rm/Plano+de+Contas+Referencial+-+Layout+3.0)
10. É obrigatório informar uma conta de centro de custo vinculada à conta referencial (plano paralelo)?  
    Resposta: Esta associação tem caráter facultativo, assim a empresa deverá avaliar se serão enviadas as informações gerenciais ou não. Verifique com o Contador da empresa.
11. Qual o plano referencial é utilizado no FCONT?  
    Resposta: Para o FCONT não houve alteração no plano referencial, neste caso poderá usar o mesmo do ano passado.
12. Empresas que já enviavam no ano anterior, terá que cadastrar novo plano de contas referencial?  
    Resposta: Para a ECD sim, pois para o ano base de 2014 o plano referencial teve alterações.
13. As contas de compensação não têm conta correspondente no plano referencial, estas contas são transitórias e não afetam o resultado. Existe a opção nos parâmetros para não enviá-las ao Sped?  
    Resposta: Em relação a não enviar as contas, basta marcar a opção de "Não Informada" no cadastro da conta contábil na opção de Classificação da Conta.
14. Caso a empresa já tenha entregue o SPED Contábil sem a associação do plano referencial e tenha a obrigatoriedade para entregar o ECF, o que deve ser feito?  
    Resposta: Para a ECF é obrigatório, assim deverá associar no TOTVS Gestão Contábil o plano referencial.
15. O plano de contas é o mesmo para o SPED, FCONT e ECF?  
    Resposta: Para as rotinas ECF e ECD os planos referenciais é o mesmo, já o FCONT não sofreu alteração e deverá ser usado o mesmo plano do ano passado.

Para maiores informações:

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE** [**R@Controladoria**](http://fluig.totvs.com/portal/p/10097/subject/rcontbil)

**Canais** **de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 2 – (Controladoria e Finanças), 5 – (Planejamento e Controle Orçamentário), 2 – (RM Saldus).
