---
content_hash: e3ff21f6912cc96a917edd05596940200ebf90afcf12c1af422f46e10305e111
fetched_at: '2026-06-29T00:10:26.111071+00:00'
page_id: '512431501'
product: rm
source: tdn-rm
title: Cadastro - Equivalência Patrimonial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=512431501
version: 35
---

O cadastro de equivalência é necessário para que o [processo](https://tdn.totvs.com/x/mxWLHg) possa gerar o lançamento contábil de equivalência patrimonial. Neste cadastro deverão ser informadas todas as informações necessárias para que o lançamento seja criado.

**Descrição:** Campo livre, de preenchimento obrigatório onde o usuário irá descrever algo que identifique a sua equivalência;

**Filial Padrão:** Deve-se informar uma filial obrigatoriamente, esta será utilizada para criação do lançamento contábil de equivalência;

**Departamento Padrão**: Campo de preenchimento facultativo, caso o usuário utilize departamento, poderá ser informado neste campo. Este campo respeita validações de parâmetros gerais do sistema;

**Centro de Custo Padrão:** Campo de preenchimento facultativo, caso o usuário utilize centro de custo, poderá ser informado neste campo. Este campo respeita validações de parâmetros gerais do sistema;

**Usar Rateio Default das contas:** Caso esse *flag* seja marcado e as contas contábeis que irão contabilizar a equivalência tenham contas gerenciais default em seu cadastro, o sistema irá utilizar essas contas gerenciais para realizar a contabilização. Caso a opção fique desmarcada o usuário deverá informar qual a conta gerencial deverá ser utilizada para a contabilização. Observação: Essa opção apenas será utilizada caso as contas contábeis responsáveis por realizar a contabilização da equivalência utilizem distribuição gerencial.

**Histórico e Complemento de Histórico:** É obrigatório informar um histórico padrão, já o complemento é de preenchimento facultativo. Ambos serão utilizados para inserir o lançamento de equivalência. Estes campos respeitam validações de parâmetros gerais do sistema.

**Grupo Empresarial:** Preenchimento obrigatório, será utilizado para filtro das coligadas investidas e no processo da equivalência para recuperação do percentual de participação dos investimentos societários.

---

Ainda é possível que alguns dos campos acima possam ser desconsiderados no momento em que o [processo](https://tdn.totvs.com/x/mxWLHg) for executado, isso se deve ao fato de que na tela de dados da apuração o usuário pode informar filial, departamento e centro de custo específicos para cada tela de dados de apuração. Os dados de apurações serão informados dentro da tela de apuração da equivalência patrimonial e podem ser um ou vários, o propósito é que seja inserido um dado apuração para cada investida que a investidora tenha.

Os campos disponíveis na tela de dados da apuração são:

**Filial:** Campo de preenchimento facultativo. Poderá ser informada nos casos onde o usuário deseja que seja utilizada uma filial diferente da cadastrada no primeiro momento na tela de apuração. Caso este campo seja informado o [processo](https://tdn.totvs.com/x/mxWLHg) irá desconsiderar a filial informada na tela de apuração e levará em consideração a filial informada neste campo. Este campo respeita validações de parâmetros gerais do sistema;

**Departamento:**Campo de preenchimento facultativo. Poderá ser informada nos casos onde o usuário deseja que seja utilizada um departamento diferente do cadastrado no primeiro momento na tela de apuração. Caso este campo seja informado o [processo](https://tdn.totvs.com/x/mxWLHg) irá desconsiderar o departamento informado na tela de apuração e levará em consideração o departamento informado neste campo. Este campo respeita validações de parâmetros gerais do sistema;

**Centro de Custo:**Campo de preenchimento facultativo. Poderá ser informada nos casos onde o usuário deseja que seja utilizada um centro de custo diferente do cadastrado no primeiro momento na tela de apuração. Caso este campo seja informado o [processo](https://tdn.totvs.com/x/mxWLHg) irá desconsiderar o centro de custo informado na tela de apuração e levará em consideração centro de custo informado neste campo. Este campo respeita validações de parâmetros gerais do sistema;

**Ganhos Participação Societária - Investimento:** Deve ser informada a conta contábil de investimento para que o lançamento de equivalência seja incluído;

**Ganhos Equivalência Patrimonial Positiva - Resultado:**Deve ser informada a conta contábil de resultado para que o lançamento de equivalência seja incluído;

**Perdas Participação Societária - Investimento:** Deve ser informada a conta contábil de investimento para que o lançamento de equivalência seja incluído;

**Perdas Equivalência Patrimonial Negativa - Resultado:**Deve ser informada a conta contábil de resultado para que o lançamento de equivalência seja incluído;

**Investida:**Aqui será informada a empresa investida, a qual será apurado o seu resultado e realizada a equivalência patrimonial na investidora.

É importante que a investida esteja cadastrada como pertencente ao  para recuperação do percentual de participação que a investidora detém sob a investida. Este percentual será utilizado, desconsiderando o Tipo de Consolidação existente na movimentação do investimento societário, quando o [processo](https://tdn.totvs.com/x/mxWLHg) for acionado.

**Ganhos** **Operações Intercompany (Eliminações):** Devem ser informadas as contas contábeis (crédito/débito) de eliminação da coligada investida para que o lançamento de equivalência seja incluído com eliminação de valores. Nestes campos são disponibilizadas para seleção as Contas Contábeis que estejam com o flag *"Eliminar valores na consolidação"* marcado.

**Perdas** **Operações Intercompany (Eliminações):** Devem ser informadas as contas contábeis (crédito/débito) de eliminação da coligada investida para que o lançamento de equivalência seja incluído com eliminação de valores. Nestes campos são disponibilizadas para seleção as Contas Contábeis que estejam com o flag *"Eliminar valores na consolidação"* marcado.

**Grupos de Contas:** Aqui serão informados os grupo(s) de contas de resultado da investida e, opcionalmente, o código do histórico padrão de cada um desses grupos. O saldo desse(s) grupo(s) será apurado, considerando o histórico padrão caso ele tenha sido informado, e posteriormente aplicado o percentual de participação informado no cadastro de controlada da investida.  
*Para preenchimento dessas informações deve-se preencher o grupo empresarial obrigatoriamente.*

É possível observar que as contas contábeis que serão utilizadas para realizar o lançamento contábil são informadas duas vezes. Entretanto será utilizado apenas duas contas para realizar o lançamento, ou as contas que foram informadas na parte de ganhos ou as contas que foram informadas na parte de perdas. A possibilidade de cadastrar contas diferentes para ganho e perda é apenas uma forma de flexibilizar e automatizar o processo para o usuário, onde as duas possibilidades serão atendidas levando em consideração a apuração das contas de resultado da investida.

Tela - Cadastro da Apuração da Equivalência PatrimonialTela - Dados da Apuração da Equivalência Patrimonial

   

Essa tela esta dentro da tela de de cadastro da apuração da equivalência patrimonial.

Veja Também

* [Processo - Equivalência Patrimonial](https://tdn.totvs.com/pages/viewpage.action?pageId=512431515)
* [Desfazer Equivalência Patrimonial](https://tdn.totvs.com/pages/viewpage.action?pageId=512431528)
* Cadastro de Controladas
