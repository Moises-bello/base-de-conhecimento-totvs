---
content_hash: 91f4d0d4e118f9f79705f25b2b885d5651331804a1a041e42b7cc58f1f26f8c1
fetched_at: '2026-06-29T00:09:32.586615+00:00'
page_id: '425458880'
product: rm
source: tdn-rm
title: Serviços Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458880
version: 47
---

---

Serviços são todas as atividades que uma instituição pode cobrar de um aluno, como por exemplo: Mensalidade, Recuperação, Apostilas etc. e estarão presentes nas parcelas dos contratos dos alunos.

A tela de cadastro dos Serviços pode ser acessada através do menu**Financeiro/Contábil | Formação de Preço | Serviços**.

Adequação à Reforma Tributária

A partir das versões **12.1.2502.264, 12.1.2506.224 e 12.1.2510.154**,, foi disponibilizado o campo **Regra Tributária** para serviços educacionais do **Ensino Superior**, localizado em: **Financeiro/Contábil → Serviço**. Acesse a aba **Integrações NFS-e.**

 O preenchimento do campo no cadastro de**Serviço** torna-se necessário quando não houver vínculo configurado nos **Parâmetros de Integração**, assegurando o correto tratamento na geração de movimento

Cada serviço possui um conjunto de atributos que serão utilizados pelo sistema durante as operações de geração das parcelas do contrato do aluno, geração e re-geração do lançamento financeiro das parcelas, contabilização dos serviços prestados e geração de movimentos para emissão de nota fiscal.  
O cadastro do Serviço e seus atributos são responsáveis por fazer o vínculo entre o TOTVS Educacional, o financeiro, o contábil e a geração de movimentos.  
Além do **código**, **nome** e **valor** do serviço prestado ao aluno, as informações dos campos presentes nos *Dados financeiros* desta tela serão enviadas para os lançamentos financeiros gerados pelo serviço prestado. Estas informações devem ser cadastradas diretamente no TOTVS Gestão Financeira.

Verifica inadimplência durante o processo de matrícula

Existem situações onde a instituição de ensino opta por não oferecer determinado serviço para alunos inadimplentes, se este for o caso, marque a opção **'Verifica inadimplência durante o processo de matrícula'** para que o serviço *não* seja oferecido a alunos inadimplentes, bloqueando a sua matrícula.

Observações

Para mais informações sobre verificação de inadimplência, podem ser acessados os links abaixo:

Permite negociação/acordo financeiro de lançamentos provenientes desse serviço

A opção **'Permite negociação/acordo financeiro de lançamentos provenientes desse serviço'** deve estar marcada para os serviços os quais a instituição permite que seja feita negociação de Acordo realizada no módulo financeiro.

Aproveita valores da conta corrente do aluno na geração de lançamentos

As instituições de ensino que desejarem trabalhar com valores na  do aluno deverão indicar quais serviços poderão aproveitar estes valores ao serem gerados lançamentos financeiros marcando a opção **'Aproveita valores da conta corrente do aluno na geração de lançamentos'** para os serviços desejados.

Considera parcelas fixas do serviço no cálculo de parcelas por crédito

No contrato dos alunos, alguns *serviços* prestados podem ter valores *fixos* ou podem ter seus valores calculados por *número de créditos*. Para que valores fixos de mais de um serviço possam ser considerados no cálculo dos valores das parcelas calculadas pelo número de créditos, a opção '**Considera parcelas fixas do serviço no cálculo de parcelas por crédito**' deve ser marcada. Assim torna-se possível definir quais serviços, além do serviço da parcela que está sendo calculada, poderão ter suas parcelas fixas consideradas no cálculo das parcelas geradas pelo número de créditos financeiros, basta que a esta opção dentro do cadastro do respectivo serviço esteja marcada. E assim, mesmo que uma parcela fixa pertença a um serviço diferente daquele que é calculado pelo número de créditos financeiros, é possível que esta parcela fixa seja considerada no cálculo dos valores das parcelas calculadas por crédito. Esta opção somente ficará habilitada se o parâmetro do sistema '*Considerar parcelas fixas na divisão de créditos financeiros entre as parcelas do contrato*' estiver marcada. Este parâmetro está disponível em *Ambiente | Parâmetros | Educacional | Integração | Financeiro | Geral 1/4*.

Disponível para o projeto de Pesquisa e ExtensãoAlguns serviços podem ser utilizados nos Workflows do projeto de Pesquisa e Extensão. Marque a opção **'Disponível para o projeto de Pesquisa e Extensão'** para indicar que este serviço pode ser utilizado neste projeto.  
Para as instituições de ensino que trabalharem com o modelo de  que inclui lançamentos de devolução, ao gerar lançamento financeiro das parcelas o sistema sempre aproveita créditos provenientes da inclusão de bolsa retroativa através da inclusão de *'Vínculos'* nos lançamentos envolvidos, possibilitando que o valor dos créditos possam ser abatidos do valor original do lançamento da parcela. Porem nem todos os serviços devem aproveitar os créditos de devolução ao serem gerados seus lançamentos financeiros, por exemplo o serviço de Xerox. Se desejar que algum serviço *não* aproveite estes créditos na geração do lançamento da parcela, *marque* a opção **'Desconsiderar crédito de bolsa retroativa'** para os serviços desejados. Considera desconto por antecipaçãoAs instituições de ensino podem cadastrar alguns descontos para serem concedidos aos alunos que quitarem antecipadamente os boletos referentes aos serviços prestados, mas para flexibilizar a sua aplicação, os  somente serão aplicados aos boletos cujos serviços tiverem a opção '**Considera desconto por antecipação**' marcados.Desconsidera na geração de Nf-e por competênciaPara que a  do serviço prestado possa ser emitida, é necessário gerar um movimento com estas características. Para isto, associe o serviço correspondente, cadastrado e parametrizado diretamente dentro do TOTVS Gestão de Estoque, Compras e Faturamento indicando-o em **Serviço RM Nucleus**.Aplicar retenção de tributos defaults definidos e do tributo IRRF para clientes pessoas jurídicas na geração de lançamento da parcela

**Aplicar retenção de tributos defaults definidos e do tributo IRRF para clientes pessoas jurídicas na geração de lançamento da parcela:** Este parâmetro marcado indica que o serviço passa a considerar a regra que, para responsáveis financeiros que sejam pessoa jurídica, seja possível carregar os [tributos defaults](https://tdn.totvs.com/display/LRM/Tributos+Default+de+Fornecedor) do cadastro do cliente, para que a [geração de lançamento](https://tdn.totvs.com/pages/releaseview.action?pageId=425459455) realize a retenção dos impostos: CSLL, COFINS, PIS (identificadas no RM com “COF RF”, “CSLL-RF”, “CS-RF”, “PIS RF”).

E a **partir dos patch's 12.1.2502.253, 12.1.2506.211, 12.1.2510.139 e da versão 12.1.2602**, também passa a considerar quando marcado para os responsáveis financeiro que sejam pessoa jurídica  conforme parametrização do  e a  vinculado ao serviço da parcela do contrato do aluno.

O valor que o TOTVS Educacional levará para a base de cálculo da retenção já será informado com o desconto da bolsa incondicional abatido. Esse valor é exibido na coluna destacada na imagem.

O campo Base de Cálculo, habilitado para preenchimento, deve ser utilizado caso o usuário deseje informar bases de cálculo específicas. Por padrão, ele apresentará o valor original do lançamento.

Aviso

A **partir dos patch's 12.1.2502.253, 12.1.2506.211, 12.1.2510.139 e da versão 12.1.2602.**

O valor que o TOTVS Educacional levará para o valor do serviço já será informado com o desconto da bolsa incondicional abatido. Esse valor é exibido no campo valor do serviço destacado na imagem.

Conforme parametrizações no  esse valor será utilizado como base de cálculo da retenção do IRRF-PJ no lançamento a receber seguindo as regras do módulo financeiro.

Permitir pagamento recorrente

Implementamos a opção dentro do cadastro de serviço para que seja possível realizar a recorrência para determinado serviço.

**Permitir pagamento recorrente:** deve estar marcada para definir se é permitido a recorrência para aquele o serviço.

O parâmetro não ficará disponível na tela caso o parâmetro **Educacional | Tesouraria | Geral 3/4 | Permite habilitar pagamento automático** estiver desmarcado, ou o sistema não esteja usando TPC.

Dados contábeis 

**Tipo Contábil:**Para fazer a integração com o sistema contábil na geração de lançamento, creditando e debitando as contas contábeis conforme o evento contábil informado nos parâmetros deste sistema, identifique o **Tipo contábil** corretamente.

**Compõe contabilização por competência:** identifica se o serviço irá compor a contabilização que pode ser gerada por competência, marcando essa opção.

**Default Contábil:** se desejar que a contabilização utilize os defaults contábeis próprios de cada serviço, cadastre-os corretamente dentro do **Default Contábil** e indique esta utilização no evento contábil utilizado. As permissões de incluir, editar e excluir defaults contábeis estão relacionadas à permissão de edição do serviço, ou seja, se o usuário não tiver permissão para editar o serviço, também não conseguirá incluir, editar ou excluir algum default contábil embora consiga visualizá-lo.

Permite pagamento

**Permite Pagamento (Novo Portal do Aluno) e eduCONNECT:** no cadastro dos Serviços do TOTVS Educacional existem quatro opções onde o usuário poderá marcar quais serviços que ele deseja que sejam pagos com Cartão de Crédito, Cartão de Débito, PIX ou Boleto.

* **Boleto**: Caso o parâmetro referente ao pagamento por boleto esteja marcado, o portal exibirá o botão para pagamento com Boleto.
* **Cartão de Crédito:** Caso o parâmetro esteja desmarcado para os dois tipos de pagamento com Cartão, o portal e app não exibirá o botão referente ao pagamento com Cartão.
* **Cartão de Débito:**
* **Pix:** Caso o parâmetro referente ao pagamento com PIX esteja marcado, o portal exibirá o botão para pagamento utilizando o Pix.  
  Para cliente que utilizam TOTVS Pagamento Digital deverá ser configurado em TOTVS Gestão Financeira | Contas a Receber | opção [TOTVS Pagamento Digital](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+receber), caso ao contrário será considerado o Pix retornado pelo banco, para saber mais sobre retorno bancário, [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=572497578).

Como padrão, o sistema manterá  a configuração predominante, caso o usuário deseje parametrizar algum serviço em específico, basta desmarcar o checkBox referente ao tipo de pagamento.

**Máximo de Parcelas Cartão de** **Crédito:** Para o gateway de pagamento CyberSource, será possível informar o número máximo de parcelas para pagamento com cartão de crédito por serviço. Esse valor terá prioridade sobre o parâmetro de número máximo de parcelas configurado na parametrização do gateway nos parâmetros do financeiro ([parametrização do gateway CyberSource](https://tdn.totvs.com/pages/releaseview.action?pageId=421388865#ModelosE-commerce-CyberSource)). Esse campo também estará disponível para o gateway Adyen ([parametrização do gateway Adyen](https://tdn.totvs.com/pages/releaseview.action?pageId=421388865#ModelosE-commerce-Adyen)).

Tabelas Opcionais

**Tabelas Opcionais:** são tabelas do TOTVS Gestão Financeira e que podem ser associadas ao serviço. Essas tabelas contêm informações direcionam de maneiras diferentes a integração com os sistemas. Elas poderão ser utilizadas se no TOTVS Gestão Financeira houver esta indicação e se nos parâmetros deste sistema (*Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin- Opcionais*) elas forem indicadas. Havendo esta indicação, as tabelas opcionais podem ainda ser definidas distintamente para cada serviço. Para isto, acesse a aba *Tabelas opcionais* e informe-as.
