---
content_hash: 5e1cc2491fadfef7c9789911b54a78fddedc6eebc7b32b0fdf60315867c0dc67
fetched_at: '2026-06-29T00:12:08.054500+00:00'
page_id: '928941770'
product: rm
source: tdn-rm
title: Vigências de Alíquota
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=928941770
version: 87
---

![](https://tdn.totvs.com/download/attachments/928941770/Vig%C3%AAncias-de-Al%C3%ADquota.png?version=1&modificationDate=1745585393100&api=v2)
]]>#FFA500#FFFACD#FFE766dashedAviso Importante:1%99%

Informamos que o cadastro de **Vigências de Alíquota** está sendo desenvolvido gradualmente. Algumas funcionalidades que não são suportadas atualmente, estarão disponíveis nas próximas Releases.  
Essa mudança é parte do nosso compromisso com a evolução tecnológica e a otimização de nossas soluções, proporcionando maior estabilidade e alinhamento com as atualizações mais recentes do mercado.

# Conteúdo

2Conteúdonone

# 1. Visão Geral

As **Vigências de Alíquota** são essenciais para a gestão tributária no contexto da reforma. Elas permitem parametrização das alíquotas dos tributos dentro de períodos específicos, assegurando que o cálculo dos impostos sejam realizados conforme cadastrados.

O cadastro é feito por coligadas e o objetivo é que os tributos como **CBS, IBS e IS** sejam aplicados corretamente, respeitando as datas definidas e a abrangência estabelecida para cada um.

Além disso, o cadastro incorpora regras que evitam inconsistências, como a validação de datas e a prevenção de registros duplicados. Dessa forma, o processo de apuração tributária torna-se mais seguro, eficiente e alinhado às novas exigências fiscais, reduzindo riscos de não conformidade e simplificando a operação dos contribuintes.

# 2. Como acessar

O cadastro de **Vigência de Alíquota** está disponível a partir da versão **12.1.2502** do TOTVS Gestão Fiscal.

IMPORTANTE!

**Mantenha o sistema sempre atualizado para o último patch disponibilizado.** Esta prática assegura que todos os ajustes e melhorias mais recentes estejam aplicados ao seu ambiente.

Para acessá-lo:

**Permissões**

* Acesse o perfil vinculado ao usuário no módulo TOTVS Gestão Fiscal.
* Vá até a aba **Acesso a Menus** e siga o caminho:  
  `[01] Cadastros` → `[01.01] Específicos` → `[01.01.11] Mais...` → selecione `[01.01.11.21] Vigência de Alíquota` e clique em **Permitir Acesso**.

Segurança - Acesso - Perfis

**Menu de Acesso**

* TOTVS Gestão Fiscal → **Cadastros** → **Específicos** → **Mais** → **Vigências de Alíquota**.

Acesso ao Menu

# 3. Campos do Cadastro

O cadastro de Vigências de Alíquota possui diversos campos que garantem a correta aplicação das alíquotas dentro do sistema.

Esse cadastro é **Multi-Coligadas,** permitindo assim a visualização dos registros de todas as coligadas onde o usuário possui acesso, facilitando a inclusão, visualização, edição e exclusão dos registros sem a necessidade de logar na coligada correspondente ao cadastro.

  
Campos

|  |  |  |  |
| --- | --- | --- | --- |
| **Campos** | **Obrigatório** | **Descrições dos Campos** | **Regras dos Campos** |
| Coligada | Sim | Código da coligada | A visualização da coligada é condicionada a permissão do usuário. |
| Identificador | Sim | Código único gerado automaticamente para cada vigência cadastrada | Deve ser apresentado na tela para visualização, mas não pode ser editado pelo usuário |
| Tributo | Sim | Especifica o tributo ao qual a alíquota se refere a CBS, IBS e IS. | Campo de busca baseado nos tributos cadastrados |
| Alíquota(%) | Sim | Permite definir um percentual da alíquota do tributo. | Não pode ser zero, para garantir a validade do cadastro. |
| Alíquota de Referência | Não | Informa se a Alíquota acima será referência | Para Estados/Municípios que não possuírem uma Vigência de Alíquota específica associada; indica que eles utilizam a Alíquota de Referência. |
| % de Redução do ICMS/ISS | Não | Permite definir o percentual de redução a ser aplicado sobre a alíquota do ICMS e do ISS durante o período de transição gradual para o IBS e CBS. Aplicável somente a partir de 2029. | Não pode ser zero, para garantir a validade do cadastro. Este campo só pode ser preenchido para os tributos ICMS e ISS. |
| % de Redução para Compras Governamentais | Não | Permite definir um percentual de redução das alíquotas de IBS e CBS nas aquisições realizadas por entes governamentais. (Art. 472 da LC 214/2025) | Campo podendo ser nulo e será visível somente quando o Tributo da Vigência de Alíquota for específico para o CBS (Contribuição sobre Bens e Serviços). |
| Inicio da Vigência | Sim | Indica a partir de quando a vigência da alíquota entra em vigor. | Usado para definir a aplicação correta da alíquota no período correspondente. |
| Fim da Vigência | Não | Define até quando a vigência da alíquota será válida. | Se preenchido, não pode ser menor que o Inicio da Vigência. |
| Descrição | Não | Campo de texto para incluir informações complementares sobre a vigência. | Não possui validações restritivas, servindo apenas para fins informativos. |

## 3.1. Regras do Cadastro

Para alterar ou cadastrar uma nova vigência as seguintes regras serão aplicadas:

| **Regra** | **Condição** | **Exemplos** |
| --- | --- | --- |
| **1. Intersecção de datas para o mesmo Tributo e alíquota** | Mesmo código do tributo + mesmo valor da alíquota + intervalo de datas coincidente (mesmo que parcial) | Imagine que já exista o seguinte registro no sistema: **Tributo IBS\_Mun, 5%, Período 01/01/2026 à 31/12/2026.**  Validações realizadas na alteração ou inclusão de um novo registro:   * IBS\_Mun, 6%, Período **01/01/2026 à 31/12/2027** Período com intersecção * IBS\_Mun, **4%**, Período 01/01/2026 à 31/12/2026A alíquota é diferente, portanto permitido. * **IBS\_UF**, 5%, Período 01/01/2026 à 31/12/2026  O Tributo é diferente, portanto permitido. |
| **2. Duplicidade de Alíquota de Referência para o mesmo Tributo e período** | Mesmo código do tributo + marcada como “Alíquota de Referência” + intervalo de datas coincidente | Imagine que já exista o seguinte registro no sistema: **Tributo** **IBS\_UF, Alíquota de Referência, 18%, 01/01/2026 a 31/12/2026**  Validações realizadas na alteração ou inclusão de um novo registro:   * Tributo IBS\_UF, Alíquota de Referência, **17%**, 01/01/2026 a 31/12/2026 Já existe uma alíquota de referência para este Tributo no mesmo período * Tributo **IBS\_Mun**, Alíquota de Referência, 18%, 01/01/2026 a 31/12/2026  O Tributo é diferente, portanto permitido. |
| **3. Alterar o período do registro que já possui vínculos com Municípios ou Estados gerando sobreposição de datas** | Alteração de datas não pode gerar conflito com outras vigências com mesmos vínculos | Imagine que já exista os seguintes registros no sistema:   1. **Tributo IBS\_Mun, 5%, Período 01/01/2026 à 31/12/2026**, associada aos Municípios de Belo Horizonte e São Paulo 2. **Tributo IBS\_Mun, 7%, Período 01/01/2027 à 31/12/2027**, associada aos Municípios de Belo Horizonte e São Paulo   Não é possível alterar a **data inicial** do segundo registro para **01/01/2026** pois irá conflitar com o primeiro registro.   * IBS, Municipal, **01/06/2025 a 20/07/2025** * IBS, Municipal, **15/07/2025 a 15/08/2025** * IBS, Municipal, **01/06/2025 a 31/08/2025** |
| **4. Alterar para Alíquota de Referência com vínculos** | Vigência vinculada a municípios ou estados não pode ser marcada como “Alíquota de Referência” | Tributo IBS\_UF, associada aos Estados de MG e SP → não pode ser alterada para Alíquota de Referência |

## 3.2. O que você precisa cadastrar ano a ano

Para **2026** você precisa apenas de dois registros no Cadastro:

1. Um registro com o tributo CBS com a alíquota de 0,9%
2. Um registro com o tributo IBS\_UF com a alíquota de 0,1%

Registros necessários para 2026

# 4. Anexo: Vigências por município

## 4.1. Sobre

Este anexo tem como finalidade vincular municípios nas alíquotas a serem aplicadas na base de cálculo de um determinado tributo para o determinado munícipio.

## 4.2. Informações sobre os campos

Tela do sistema

* **Código do Município**: Campo de busca (Lookup) com todos os municípios

## 4.3. Regras da vigência por município

Para vincular um município em uma vigência as seguintes regras não deverão ser violadas:

| **Regra** | **Condição** | **Exemplo de Situação Não Permitida** |
| --- | --- | --- |
| 1. Coincidência de vigência municipal com vínculo | Já existir vigência com mesmo código do tributo, abrangência **Municipal** e vínculo com município, cujo intervalo de datas coincida, mesmo que parcialmente | Vigência: IBS, Municipal, **01/07/2025 a 31/07/2025**, vínculos: Belo Horizonte e São Paulo → não pode haver:   * IBS, Municipal, **01/06/2025 a 20/07/2025**, vínculo: Belo Horizonte * IBS, Municipal, **15/07/2025 a 15/08/2025**, vínculo: São Paulo * IBS, Municipal, **01/06/2025 a 31/08/2025**, vínculo: Belo Horizonte |
| 2. Coincidência com Alíquota de Referência | Vigência marcada como **Alíquota de Referência** na abrangência Municipal não pode ter vínculo com municípios | IBS, Municipal, **Alíquota de Referência** → não pode ter vínculo com município |
| 3. Abrangência diferente de Municipal | Não é permitido vincular município a vigência cuja abrangência não seja Municipal | CBS, Federal → não pode vincular município |

# 5. Anexo: Vigências por estado

## 5.1. Sobre

Este anexo tem como finalidade vincular estados nas alíquotas a serem aplicadas na base de cálculo de um determinado tributo para o determinado estado.

## 5.2. Informações sobre os campos

Tela do sistema

* **Código do Estado**: Campo de busca (Lookup) com todos os estados

## 5.3. Regras da vigência por Estado

Para vincular um estado em uma vigência as seguintes regras não deverão ser violadas:

| **Regra** | **Condição** | **Exemplo de Situação Não Permitida** |
| --- | --- | --- |
| 1. Coincidência de vigência estadual com vínculo | Já existir vigência com mesmo código do tributo, abrangência **Estadual** e vínculo com estado, cujo intervalo de datas coincida, mesmo que parcialmente | Vigência: IBS, Estadual, **01/07/2025 a 31/07/2025**, vínculos: MG e SP → não pode haver:   * IBS, Estadual, **01/06/2025 a 20/07/2025**, vínculo: MG * IBS, Estadual, **15/07/2025 a 15/08/2025**, vínculo: SP * IBS, Estadual, **01/06/2025 a 31/08/2025**, vínculo: MG |
| 2. Coincidência com Alíquota de Referência | Vigência marcada como **Alíquota de Referência** na abrangência Estadual não pode ter vínculo com estados | IBS, Estadual, **Alíquota de Referência** → não pode ter vínculo com estado |
| 3. Abrangência diferente de Estadual | Não é permitido vincular estado a vigência cuja abrangência não seja Estadual | CBS, Federal → não pode vincular estado |

# 6. Processo: Cópia de Vigências (para outras coligadas)

## 6.1. Sobre

Este processo possibilita ao usuário o reaproveitamento dos registros de alíquotas e seus estados/municípios que foram criados e organizados em uma coligada através da cópia para outras coligadas evitando assim retrabalho e erros.

A cópia será validada conforme os registros existentes na coligada destino: tributo, abrangência, interseção de datas, referência, registros nos anexos de estados/municípios de acordo com a o tipo de abrangência do tributo (ver mais detalhes nas regras do cadastro de Vigência de alíquotas).

## 6.2. Informações sobre a execução do processo

O processo pode ser acessado através do TOTVS Gestão Fiscal | *Cadastros | Na divisão de "Específicos" opção Mais | Vigências de Alíquota* e então na menu de processos *"Cópia de vigências".*

Tela do sistema

Registros de Vigência de alíquota com anexos de municípios e estados

Acionamento do processo

Seleção das coligadas destino

Execução e LOG do processo

LOG do processo com tela expandida (opção: Abrir no editor)

Visão de Vigências de alíquotas após a execução do processo

## 6.3. Regras do processo de Cópia de Vigência de alíquotas

Para acessar o processo não há nenhuma regra específica que precise ser observada.

No caso da cópia — ou seja, a inclusão dos registros de vigência de alíquotas nas demais coligadas — o sistema seguirá as regras definidas no cadastro de vigências. Nos anexos de municípios e estados serão respeitadas também as regras para inclusão de municípios e/ou estados conforme descrito anteriormente, caso seja necessário consultá-las.

O processo sempre tentará incluir uma cópia do registro de origem na coligada de destino. Se já existir na coligada de destino um registro de vigência com as mesmas características do registro que se pretende copiar o sistema emitirá um erro e não continuará o processamento desse registro passando ao próximo.

Nos anexos de municípios e estados, caso alguma regra de inclusão seja violada, o sistema manterá o registro de vigência de alíquota, porém não incluirá os respectivos registros de municípios e/ou estados associados a essa vigência.

![](https://tdn.totvs.com/download/attachments/928941770/Cadastro%20de%20Vig%C3%AAncia%20de%20Al%C3%ADquotas%20-%20Footer.jpg?version=1&modificationDate=1743504038097&api=v2?version=1&modificationDate=1742918628907&api=v2)
]]>

**Quer contribuir com a evolução da nossa documentação? [Clique aqui e dê um feedback sobre esta página!](https://forms.gle/RZXc3eYwhuq9TNtD6)**
