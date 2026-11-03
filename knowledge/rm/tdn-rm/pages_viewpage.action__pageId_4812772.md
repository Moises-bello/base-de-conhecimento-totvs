---
content_hash: 408028b4fdcc4c57b6c030b6982d9201d54c321794f068e5c8bb8d0c7cb240c6
fetched_at: '2026-06-29T00:10:18.908242+00:00'
page_id: '4812772'
product: rm
source: tdn-rm
title: MANAD - Dicas e Soluções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4812772
version: 4
---

BLOCK

MANAD - Dicas e Soluções

FAQ: **MANAD - Dicas e Soluções**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | 10.80 e posteriores |

Avaliação

**Produto:** TOTVS Folha de Pagamento**Versão:**10.80   
**Processo de Negocio:** Administração de Pessoal  
**Processo do Sistema:** MANAD  
**Subprocesso:** Validação e correção dos erros do arquivo MANAD  
  
  
MANAD é o Manual Normativo de Arquivos Digitais no qual consta todas as informações para gerar o arquivo digital a ser apresentado à fiscalização da Secretaria da Receita Previdenciária quando a empresa for intimada por Auditor Fiscal da Previdência Social (AFPS).

Antes de executar o procedimento aqui descrito, recomendamos a leitura do manual explicativo do MANAD, disponível no site da Receita Federal, bem como o download, instalação e a leitura do manual do aplicativo SVA, que é o programa validador do arquivo (também disponível no site da Receita).

É importante estar com a versão do sistema e da Biblioteca atualizada para a geração do arquivo.

Solução

**Informações dos Blocos:**

**Os blocos que começam com 0 (zero) são o cabeçalho do arquivo. O restante dos blocos gerados pelo TOTVS Folha de Pagamento (RM Labore) começa com a letra K, exceto o Bloco I050 (que leva o cadastro de Plano de Contas Contábeis) e o bloco I100 (que leva o cadastro de Centros de Custos).**

**Deve ser gerado também um arquivo do MANAD com informações do sistema de contabilidade da empresa.**

**Detalhes das informações de cada bloco podem ser verificados pelo manual do MANAD que contém o layout do arquivo.**

**Bloco 0000** – Contém os dados das filiais ou das seções (de acordo com o parâmetro escolhido na geração do relatório).

**Bloco 0050** – Dados do contabilista informados na geração.

**Bloco 0100** – Dados do responsável pela geração do arquivo, informado na geração.

**Bloco I050** – Cadastro do Plano de contas contábil.

**Bloco I100** – Cadastro dos Centro de Custos.

**Bloco K050** – Cadastro dos funcionários.

**Bloco K100** – Cadastro de lotações (Seções).

**Bloco K150 –** Cadastro de Rubricas (Eventos).

**Bloco K200 –** Parametrização da contabilização. Eventos, seções ou centros de custos e suas contas.

**Bloco K250 –** Mestre da folha de pagamento. Leva uma linha para cada tipo de folha do funcionário, com a base de INSS e IRRF total do mês competência.

**Bloco K300 –** Itens da folha de pagamento. Leva os eventos da ficha financeira e a indicação de incidência em INSS e IRRF. O total desses eventos deve corresponder à base total informada no Bloco K250.

**Procedimentos:**

**Informações Gerais:**

- A base levada para o K250 de INSS e IRRF é por competência, isto é, a base de IRRF não irá conferir com a folha analítica se utilizar mês caixa. Isto está de acordo com o Manual do MANAD.

- Para compor a base é considerada a incidência atual do evento, se ela foi alterada, também não irá conferir com a folha da época. Com exceção dos eventos com Código de Cálculo 62 e 99. Para eles o sistema irá verificar a data informada em Opções | Parâmetros | RM Labore | Parâm. Rescisão.

- A opção de gerar o bloco K200 por Centro de custo, bem com a opção de gerar o arquivo por tomador de serviço, está informada como Parâmetros Específicos da Coligada. Estes blocos podem ser visualizados, clicando no ícone marcado conforme imagem abaixo, na tela de Seleção de Coligadas.

Lembre-se que a opção de gerar por tomador só ficará visível quando a opção “Utiliza Tomadores de Serviço” estiver marcada em Opções | Parâmetros | RM Labore | Parâm. De Cálculo.

**[![clip_image002](http://lh5.ggpht.com/_G7KXZLoZDsY/TGwqmRDPaKI/AAAAAAAAAyE/C7uw59hejA4/clip_image002_thumb%5B1%5D.jpg?imgmax=800 "clip_image002")](http://lh6.ggpht.com/_G7KXZLoZDsY/TGwql7mCajI/AAAAAAAAAyA/GGlwb-xuEZI/s1600-h/clip_image002%5B4%5D.jpg)**

**-** A utilização de filtros também está disponível somente como parâmetro específico por coligada.

**Importante!**

**Ao final da geração do arquivo, é apresentado um log. Nesse log temos informações de erros e inconsistências na geração do arquivo. Para salvar é necessário clicar em Copiar e em seguida Bloco de Notas. Este log deve ser enviado ao suporte para a solução de problemas.**

**[![clip_image004](http://lh3.ggpht.com/_G7KXZLoZDsY/TGwqncKBrTI/AAAAAAAAAyM/66Txe-BqQDE/clip_image004_thumb%5B1%5D.jpg?imgmax=800 "clip_image004")](http://lh3.ggpht.com/_G7KXZLoZDsY/TGwqm-7v94I/AAAAAAAAAyI/Cp_VEfq-1B8/s1600-h/clip_image004%5B4%5D.jpg)**

**Como corrigir problemas identificados no Log:**

**Funcionário XXX com histórico de seção inconsistente!**

Abrir o cadastro do funcionário, aba Registro | Admissão. Se o tipo de admissão for E ou T, verificar a data de Transferência nesta mesma tela. Exatamente essa data deve existir em Registro | Hist. Seção.

Para os outros tipos de admissão, a data de admissão deve existir no histórico.

**Funcionário XXX com histórico de função inconsistente!**

Mesma conferência da seção, porém, há a comparação das datas com o histórico de função em Registro | Hist. Função.

**Funcionário X - coligada Y sem cod. de categoria! Funcionário não foi incluído no arquivo!**

Informar a categoria para o funcionário no seu cadastro em Registro | FGTS/SEFIP/INSS, campo Categoria.

Se for autônomo do TOTVS Gestão Financeira (RM Fluxus) / TOTVS Gestão de Estoque, Compras e Faturamento (RM Nucleus), verificar a categoria no Lançamento do mês em questão.

[![clip_image006](http://lh4.ggpht.com/_G7KXZLoZDsY/TGwqoTY2YcI/AAAAAAAAAyU/HPajCOQ5Gxw/clip_image006_thumb%5B1%5D.jpg?imgmax=800 "clip_image006")](http://lh5.ggpht.com/_G7KXZLoZDsY/TGwqn_G9oLI/AAAAAAAAAyQ/Cd_s3cibAu4/s1600-h/clip_image006%5B4%5D.jpg)

**A conta de número XXX está sem a Natureza Contábil.**

Informar a natureza da conta especificada em Cadastro | Contabilização | Plano de contas contábeis, campo Natureza da conta para emissão do SPED .

**Lançamento com competência anterior à Admissão do funcionário X - coligada Y!**

Verificar a data de pagamento dos eventos na ficha financeira do funcionário. Existem eventos com data anterior à admissão.

**Erro ao copiar o arquivo X para a pasta Y:**

A pasta de destino deve estar com permissão total para todos os usuários e não somente para o usuário logado. Este erro não impede a geração do arquivo, o arquivo é gerado no diretório de instalação do sistema, dentro da pasta RM.Net/ExecutionData , impede somente a cópia para a pasta de destino. Assim pode ser copiado manualmente desse caminho.

**Validando o arquivo no SVA a partir da versão 3.0:**

O SVA é um sistema de Validação e Autenticação de Arquivos onde o MANAD deve ser importado para verificação de erros básicos e que impedem a entrega do arquivo para o fiscal.

**Ele é apenas um validador de uso da empresa, não transmite o arquivo**. O arquivo pode ser importado mais de uma vez, e deve ser entregue ao fiscal o próprio arquivo texto gerado após a correção dos erros apresentados.

[![clip_image008](http://lh5.ggpht.com/_G7KXZLoZDsY/TGwqpV_XvhI/AAAAAAAAAyc/rwayGZnXaSs/clip_image008_thumb%5B1%5D.jpg?imgmax=800 "clip_image008")](http://lh6.ggpht.com/_G7KXZLoZDsY/TGwqowuCP6I/AAAAAAAAAyY/jleZHFUvUrQ/s1600-h/clip_image008%5B4%5D.jpg)

Clique em Adic. Arquivos e em seguida Validar Arquivos.

[![clip_image010](http://lh5.ggpht.com/_G7KXZLoZDsY/TGwqqnMeP5I/AAAAAAAAAyk/7JZafBnYYZI/clip_image010_thumb%5B1%5D.jpg?imgmax=800 "clip_image010")](http://lh3.ggpht.com/_G7KXZLoZDsY/TGwqp1tng3I/AAAAAAAAAyg/0a_HY4r8-9s/s1600-h/clip_image010%5B4%5D.jpg)

Clique em Resultado da Validação I Mensagens da Validação

[![clip_image012](http://lh5.ggpht.com/_G7KXZLoZDsY/TGwqrkGSgdI/AAAAAAAAAyw/_yL-QKw75d4/clip_image012_thumb%5B1%5D.jpg?imgmax=800 "clip_image012")](http://lh6.ggpht.com/_G7KXZLoZDsY/TGwqrIjlZcI/AAAAAAAAAyo/rJAe0Z0KsJ8/s1600-h/clip_image012%5B4%5D.jpg)

**Registro -** é o bloco onde ocorreu o erro.

**Nº linha -** se refere à linha no arquivo importado que possa ser localizada pelo bloco de notas com o comando CTRL + G.

**Tp Msg -** pode ser Erro ou Aviso. Lembrando que mesmos os avisos devem ser acertados, a não ser que tenham justificativas.

**Mensagem -** É a mensagem detalhada do erro

**Observação -** Mais um detalhe do erro, pode ser o número da chapa, o número da conta, depende a que se refere.

Clicando com o botão direito na linha do erro, existe a opção: Exibir Registro Completo da Linha Selecionada. Demonstrado abaixo. Assim não é preciso localizar pelo bloco de notas.

[![clip_image014](http://lh5.ggpht.com/_G7KXZLoZDsY/TGwqso-KxiI/AAAAAAAAAy4/xVM3v_IFP-o/clip_image014_thumb%5B1%5D.jpg?imgmax=800 "clip_image014")](http://lh4.ggpht.com/_G7KXZLoZDsY/TGwqsMl3e0I/AAAAAAAAAy0/_MjcLlBlH2I/s1600-h/clip_image014%5B4%5D.jpg)

**Dicas para correção de erros na validação:**

**Primeiramente devemos acertar TODOS os erros de cadastro detectados pelo Log.**

**Ao importar o arquivo no SVA ocorre o erro: A versão do arquivo (003) é diferente da versão esperada (002)!**

**[![clip_image016](http://lh6.ggpht.com/_G7KXZLoZDsY/TGwqttCbhTI/AAAAAAAAAzA/B18-QgNrNGo/clip_image016_thumb%5B2%5D.jpg?imgmax=800 "clip_image016")](http://lh6.ggpht.com/_G7KXZLoZDsY/TGwqs2W2ljI/AAAAAAAAAy8/SzAL-XJHHbM/s1600-h/clip_image016%5B5%5D.jpg)**

Na tela anterior, está sendo marcada a opção grifada abaixo, sendo que a correta é a (IN SRP 12/2006)

[![clip_image018](http://lh5.ggpht.com/_G7KXZLoZDsY/TGwquiCe1yI/AAAAAAAAAzI/RByMZTj1Tzw/clip_image018_thumb%5B2%5D.jpg?imgmax=800 "clip_image018")](http://lh6.ggpht.com/_G7KXZLoZDsY/TGwquJY5N-I/AAAAAAAAAzE/JFYwuTSbano/s1600-h/clip_image018%5B5%5D.jpg)

**Ao importar o arquivo no SVA ocorre o seguinte erro: Divergência entre a quantidade de registros existentes e a quantidade informada no registro 9900.**

Atualizar a versão do sistema, o arquivo gerado está no layout do SVA aceito até a versão 2.6.

**I050 – Conta superior não localizada no registro I050**

O bloco I050 leva o número da conta contábil, no campo ao lado deve ser informada a conta superior. Assim, se a conta é a 01.02.1, a superior é a 01.02, ela deve existir no Plano de Contas. Se a conta 01.02 existir, mas estiver sem natureza esse erro também ocorre.

**K050 - Nenhum segurado contribuinte individual foi informado nos registros de cadastro de trabalhadores**

Não existe autônomo ou diretor no arquivo. Se realmente não existe o caso na empresa ou o cliente excluiu esses funcionários da geração do arquivo, pode ser desconsiderado.

**K050 – PIS/NIT Ausente ou CPF Ausente**

Verificar no cadastro do funcionário se está informado o PIS/NIT ou o CPF.

No caso de estagiários o cliente pode justificar para o fiscal ou excluí-los da geração do arquivo se o fiscal permitir.

**K050, K100, K250 ou K300 - campo obrigatório está vazio no arquivo de origem CNPJ\_CEI**

Se o bloco for o K100, verificar na linha do erro o número da seção informada, editar a seção e verificar se está com o flag “Identificação por CNPJ” marcado.

Se for outro bloco, verificar pela linha do erro a chapa do funcionário, provavelmente está com histórico de seção inconsistente.

**K200 – Conta não localizada no registro I050 – XXXX (Número da conta)**

Verificar se a conta está sendo levada para o arquivo no bloco I050, se estiver, será resolvido quando informar o indicador de natureza na conta contábil.

**K250 – Data anterior ao período das informações identificado no registro 0000**

Ir à linha do erro, localizar a chapa do funcionário. Verificar se a movimentação é de férias.

Provavelmente o arquivo está sendo gerado com início, por exemplo, 01/02/2007 e as férias foram pagas com data 29/01/2007. Este é um aviso e pode ser desconsiderado.

**K250 ou K300 – Duplicidade de registro (mesma chave de outro registro existente).**

Verificar pela linha do erro, a chapa do funcionário e o mês a que se refere. Conferir se existem dados na ficha financeira normal e também na complementar, se estiver nos dois lugares, apagar em um deles.

O script abaixo realiza a cópia da PFFINANCCOMPL para PFFINANC e depois exclui os registros da PFFINANCCOMPL corrigindo o erro acima. Lembrando que deve ser feito o backup da base antes de rodar o Script.

Script para base SQL :

INSERT INTO PFFINANC

SELECT \* FROM PFFINANCCOMPL WHERE EXISTS (SELECT \* FROM PFFINANC WHERE PFFINANCCOMPL.CODCOLIGADA=PFFINANC.CODCOLIGADA

AND PFFINANCCOMPL.CHAPA=PFFINANC.CHAPA

AND PFFINANCCOMPL.ANOCOMP=PFFINANC.ANOCOMP

AND PFFINANCCOMPL.MESCOMP=PFFINANC.MESCOMP

AND PFFINANCCOMPL.NROPERIODO=PFFINANC.NROPERIODO

AND PFFINANCCOMPL.CODEVENTO<>PFFINANC.CODEVENTO)

GO

DELETE FROM PFFINANCCOMPL WHERE EXISTS

(SELECT \* FROM PFPERFFCOMPL, PFFINANC WHERE

PFFINANCCOMPL.CODCOLIGADA=PFPERFFCOMPL.CODCOLIGADA

AND PFFINANCCOMPL.CHAPA=PFPERFFCOMPL.CHAPA

AND PFFINANCCOMPL.ANOCOMP=PFPERFFCOMPL.ANOCOMP

AND PFFINANCCOMPL.MESCOMP=PFPERFFCOMPL.MESCOMP

AND PFFINANCCOMPL.NROPERIODO=PFPERFFCOMPL.NROPERIODO

AND PFFINANCCOMPL.CODCOLIGADA=PFFINANC.CODCOLIGADA

AND PFFINANCCOMPL.CHAPA=PFFINANC.CHAPA

AND PFFINANCCOMPL.ANOCOMP=PFFINANC.ANOCOMP

AND PFFINANCCOMPL.MESCOMP=PFFINANC.MESCOMP

AND PFFINANCCOMPL.NROPERIODO=PFFINANC.NROPERIODO

AND PFFINANCCOMPL.CODEVENTO=PFFINANC.CODEVENTO)

GO

DELETE PFPERFFCOMPL WHERE EXISTS

(SELECT \* FROM PFPERFF WHERE PFPERFF.CODCOLIGADA=PFPERFFCOMPL.CODCOLIGADA

AND PFPERFF.CHAPA=PFPERFFCOMPL.CHAPA

AND PFPERFF.ANOCOMP=PFPERFFCOMPL.ANOCOMP

AND PFPERFF.MESCOMP=PFPERFFCOMPL.MESCOMP

AND PFPERFF.NROPERIODO=PFPERFFCOMPL.NROPERIODO)

**Matrícula CEI com tamanho inválido**

Verificar pela linha do arquivo a qual seção o erro se refere. Se utilizar CEI, conferir o número informado. Se a seção for identificada por CNPJ, não informar nada no campo CEI.

Caso o campo CEI esteja desabilitado, acesse Opções | Parâmetros | Globais | Seção e marque a opção “Utiliza CEI”. Acesse o cadastro da seção e delete a informação no campo CEI.

**Não foi localizado o registro de encerramento do bloco K**

O arquivo não foi concluído com sucesso, verificar a mensagem de erro no Log de geração do MANAD ou se foi apresentada alguma mensagem na tela do sistema.
