---
content_hash: 3df40de25767379e0599f6618fec9e473d3041b836642f55268878955d34c49a
fetched_at: '2026-06-29T00:11:04.083735+00:00'
page_id: '624961718'
product: rm
source: tdn-rm
title: Backup - TOTVS Construção Gestão de Imóveis - Cópia de Dados ( Valores de Integração
  dos Componentes )
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=624961718
version: 1
---

**Tudo sobre Cópia de Dados** : [Clique aqui !](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=592067102)

Cópia de Dados TCGI.Cópia de Componentes |

No processo de cópia de coligadas, disponível em Serviços Globais | Cópia de coligadas ,  passa a ser possível realizar a cópia dos valores de integração dos componentes do TCGI. 

Processo deve ser feito em **3 Camadas** para que possa ser executado o processo.

Serviços Globais | Administração | Cópia de Dados | Cadastro de Entidades

**Entidade :** Componentes de Valores de Integração

Selecionando a Entidade ( Componentes de Valores de Integração ) Para este novo Tamplate.

Clicar em Incluir Selecionada e Salvar em seguida. Faça isso para todas as entidades que deseja copiar ao mesmo tempo.

Antes de executar o processo de cópia, tem que sair da tela e ir no menu:  Ambiente | Segurança de Jobs Fracionáveis.

Cadastrar um Job Fracionado para a Cópia de Coligada.  Escolha o perfil do seu usuário e coloque a classe no lookup de Classes de Job: GlbCopiaColigadaProc.

Agora, execute o processo de Cópia de Dados

Selecionar o Template e em seguida : Processos | Cópia de Dados.

Agora, execute o processo de Cópia de Dados

Selecionar o Template e em seguida : Processos | Cópia de Dados

Selecionar a Coligada Destino e em seguida : Executar

Cópia de Modalidade

No processo de cópia de coligadas, disponível em Serviços Globais | Cópia de coligadas ,  passa a ser possível realizar a cópia das Modalidades do TCGI. 

Processo deve ser feito em **3 Camadas** para que possa ser executado o processo.

Só serão copiadas as modalidade que não sejam globais. Caso a modalidade já exista no destino não será copiada de novo e nem será sobreposto os valores, por segurança do processo. A chave de verificação na coligada de destino é a descrição, data de início, tipo de modalidade e tipo de restrição. Caso algum desse valor não bata, então será criado uma nova modalidade no destino

Serviços Globais | Administração | Cópia de Dados | Cadastro de Entidades

Cadastro de template , criando um Template novo do Imobiliário

Selecione a entidade no lookup e em seguida : Incluir Selecionada e Salvar. Faça isso para todas as entidades que deseja copiar ao mesmo tempo.

Antes de executar o processo de cópia, tem que ir no menu:  Ambiente | Segurança de Jobs Fracionáveis. Cadastre um Job Fracionada para a Cópia de Coligada.  Escolhe o perfil do seu usuário e coloque a classe no lookup de Classes de Job: GlbCopiaColigadaProc.

Selecionar o Template e em seguida : Processos | Cópia de Dados

Selecionar a coligada Destino.

Executar o processo.

Modalidades Origem.

Modalidades no Destino.
