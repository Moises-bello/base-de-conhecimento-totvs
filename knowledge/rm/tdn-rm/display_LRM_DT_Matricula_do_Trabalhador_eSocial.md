---
content_hash: 2b3f35e4500d0b2ccc370264e96e953583dc0617137bc2fc99b19ff4c19c5ea4
fetched_at: '2026-06-29T00:06:29.228232+00:00'
page_id: '234455088'
product: rm
source: tdn-rm
title: DT_Matricula_do_Trabalhador_eSocial
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Matricula_do_Trabalhador_eSocial
version: 7
---

# Matrícula do Trabalhador e-Social

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *eSocial* | Matrícula do Trabalhador | |
| **Versão/Release:** | 12.1.10 |

## Descrição

Com a implantação do e-Social, o governo exige que cada empresa informe uma identificação única para o funcionário, que é o campo “matrícula eSocial” presente no layout de todos os eventos do trabalhador com vínculo empregatício.  
Para o eSocial a identificação é única para um vínculo de trabalho, que começa com a admissão do funcionário e se encerra com a demissão.  Mesmo ocorrendo transferências do funcionário entre estabelecimentos a matrícula eSocial permanecerá a mesma.  
A matrícula será gerada automaticamente pelo sistema de acordo regras parametrizadas, no intuito de manter a unicidade da informação.  
A seguir, serão esclarecidos os momentos em que a “matrícula” do e-Social será gerada e sua devida regra para preenchimento automático

## Procedimento para Utilização

**Parametrização**

As regras para preenchimento do campo são definidas pelo usuário e parametrizadas no sistema, informando qual comportamento o sistema deve considerar para o preenchimento do campo Matrícula e-Social.

Caminho: aba “**Configurações**” / botão “**Parametrizador**” / opção “**06.07 – eSocial**” / etapa “**Configurações Gerais**”/ box “**Máscara para Matrícula do Trabalhador**”

Regras:

* A Matrícula é gerada por coligada, podendo se repetir quando houver transferência de funcionário entre estabelecimentos (matriz/filial)
* A Matrícula tem 3 campos com tamanho para definir a máscara de preenchimento (Prefixo, Coligada, Sequencial)
* O campo prefixo é opcional, pois ele atenderá matrículas criadas para empresas que tem bases de dados separadas por coligada
* Os 3 campos deverão ser preenchidos conforme valores e regras abaixo:  
   - Prefixo = Vazio ou texto informado pelo usuário (opcional)  
   - Coligada = poderá receber o tamanho mínimo 3 caracteres (incluindo letra “C”)   
   - Sequencial = poderá receber o tamanho mínimo de 7 (incluindo letra “S”)
* Caso o usuário tenha alterado o tamanho para maior que 7, e depois tentar volta, será verificado se já foi gerada alguma matrícula com tamanho maior e não permitirá a alteração.
* O Tamanho máximo para a montagem da matrícula envolvendo os 3 campos de configuração será 30 caracteres.

**Admissão do funcionário**

Na admissão do funcionário (inclusão de novo funcionário na base) o processo de geração da matrícula do e-Social é transparente. O preenchimento do campo é automático, baseando-se na parametrização.

O campo matrícula no cadastro do funcionário não será obrigatório (para não interferir nas rotinas atuais do cliente), e não é editável para digitação pelo usuário. Ele será preenchido na inclusão do funcionário (após o click de inclusão), e ele não poderá ter o valor editado após o registro do funcionário estar salvo.

Caso os campos estejam vazios no parametrizador, não será gerado a matrícula e-Social, até que o usuário preencha os campos.

O campo matrícula será preenchido conforme regra abaixo:  
 - Se usa prefixo, a montagem da matrícula receberá o campo Prefixo informado no parametrizador , caso não esteja preenchido, não será considerado na geração da matrícula.  
 - Campo Coligada receberá a letra C e um sequencial conforme o tamanho informado no parametrizador .  
 Ex.: tamanho 3 e coligada = 1, deverá receber C01  
 -  Campo Sequencial receberá a letra S e um número sequencial conforme o tamanho informado no parametrizador. Este número sequencial será por coligada. Ex.: tamanho 7 e último valor da matrícula gerado foi por exemplo 000002, a próxima matrícula de uma admissão deverá receber o valor S000003.

A matrícula do e-Social não é obrigatória para funcionários que não possuem vínculo empregatício (Estagiário, Autônomos, Diretores sem vínculo, Dirigente Sindical). Neste caso existe um tratamento de não preencher o campo quando o cadastro não atender a regra.

**Processo preenchimento da matrícula e-Social**

Este processo é a ferramenta para preenchimento de forma automática e em massa do campo “Matrícula eSocial”, reduzindo o trabalho individual e manual.

Considerando que já existem dados legado na base, é importante que antes do envio para inclusão no e-Social seja gerado para cada funcionário apto o número único de matrícula.

As regras consideradas para o preenchimento automático são as mesmas da admissão, baseadas na parametrização citada no início desse documento. Caso falte a parametrização para alguma coligada selecionada, será apresentado no log de erro.

**Exemplo:**

Log de conclusão do processo:

Log de conclusão do processo - parte dos erros (coligada 7 faltando parametrização):

O processo será executado para todos os funcionários de cada coligada selecionada, com as seguintes exceções:

* Funcionários em "Saída transferência" (que estão com situação Demitido e código de afastamento 5 ou 6)
* Funcionários que já possuam valor preenchido no campo Matrícula eSocial
* Funcionários sem vínculo empregatício (Estagiários, Autônomos, Diretores sem vínculo, Dirigente Sindical)

Para habilitar o menu “Preencher a Matricula eSocial” devemos seguir os passos abaixo:

Caminho para acessar o processo:

Filtros do processo (apenas seleção de coligadas):

**Transferência Individual de Funcionário**

A transferência de funcionários entre estabelecimentos possui situações diferentes, em que pode ou não ser obrigatório a geração de nova matrícula para o funcionário transferido.  
Em resumo, sempre que a raiz do CNPJ (8 primeiros dígitos) do novo estabelecimento for diferente do estabelecimento antigo, uma nova matrícula será gerada, caso contrário o sistema mantém a mesma matrícula por se tratar de uma mesma empresa.

Abaixo seguem os passos demonstrando quando há geração de nova matrícula e-Social:

Ao efetuar a demissão do funcionário selecionando os tipos de demissão “5” ou “6” (tipos de transferência), será habilitado o botão “Transferir Funcionário”. Ele inicia o processo parametrização da transferência:

Quando a transferência for para a mesma coligada, o campo “Motivo da Transferência” é desabilitado e a opção “Estabelecimentos da própria empresa” fica marcado por padrão, e neste caso a matrícula existente é reaproveitada. Mas quando a transferência for para coligada diferente, será habilitado o campo “Motivo da Transferência”.  
Se o motivo de transferência informada for “Sucessão, incorporação, cisão ou fusão” ou “Empresa do mesmo grupo econômico”, será gerada uma matrícula diferente por se tratar de outra empresa (outra raiz CNPJ). Porém, se a raiz do CNPJ da nova coligada for o mesmo da coligada de origem, será habilitada e marcada SOMENTE a opção “Estabelecimentos da própria empresa”, e neste caso não será gerada nova matrícula, mantendo a mesma que o funcionário já possui, pois trata-se da mesma empresa.

Cadastro do funcionário antes de processar a transferência. Observe a chapa e matrícula anterior:

Cadastro do funcionário após processar a transferência. Observe que foi gerado uma nova chapa e matrícula:

**Transferência Coletiva de Funcionários**

A transferência coletiva funciona com as mesmas regras da transferência individual, porém o processo é executado para um lote de funcionários.  
Ao efetuar o processo de “rescisão coletiva” selecionando os tipos de demissão “5” ou “6” (tipos de transferência), será exibido o campo “Motivo da Transferência”.  
Se a transferência for para a mesma coligada, o campo “Motivo da Transferência” é desabilitado e a opção “Estabelecimentos da própria empresa” fica marcado por padrão, neste caso todas as matrículas existentes serão reaproveitadas (não gera matrícula).  
Porém se a transferência for para coligada diferente, será habilitado o campo “Motivo da Transferência” para seleção.  
Se o motivo de transferência informada for “Sucessão, incorporação, cisão ou fusão” ou “Empresa do mesmo grupo econômico”, serão geradas matrículas diferentes por se tratar de outra empresa (outra raiz CNPJ).  
Porém, se a raiz do CNPJ da nova coligada for o mesmo da coligada de origem, será habilitada e marcada SOMENTE a opção “Estabelecimentos da própria empresa”, e neste caso não serão geradas novas matrículas, mantendo a mesma matrícula que cada funcionário já possui, pois trata-se da mesma empresa.

Lote de funcionários na coligada de origem antes da transferência (observe as matrículas e chapas):

Quando for transferência mesma coligada:

Quando for transferência para coligada diferente:

Funcionários transferidos na coligada de destino após a transferência.  
Foram geradas novas chapas sequenciais e **novas matrículas**, mantendo o mesmo identificador.  
A regra para geração das matrículas é baseada na parametrização da coligada de destino.
