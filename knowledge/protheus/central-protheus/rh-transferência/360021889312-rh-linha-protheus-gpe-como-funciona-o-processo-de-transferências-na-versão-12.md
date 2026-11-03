---
article_id: 360021889312
category: RH - Transferência
content_hash: cb8dde47c5f7de6d72c286b79302a9125a6d84ad6fca7d0bc7ecb823bf5a222e
fetched_at: '2026-06-28T22:43:23.317713+00:00'
product: protheus
section_id: 360010781974
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona o processo de transferências na versão
  12
type: support-article
updated_at: '2025-12-16T14:12:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021889312-RH-Linha-Protheus-GPE-Como-funciona-o-processo-de-transfer%C3%AAncias-na-vers%C3%A3o-12
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24308874731543) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
Como funciona o processo de transferência de funcionários entre filiais, empresas, centro de custo, entre outras opções?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**  
O Sistema disponibiliza os seguintes tipos de transferências:

* **Transferências entre Empresas/Filiais:** Neste tipo de transferência, o funcionário é enviado para a nova empresa/filial, onde é feito movimentação de tabelas dependendo do tipo da transferência. Consulte as movimentações de tabelas [aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057237614-RH-Linha-Protheus-GPE-Movimenta%C3%A7%C3%A3o-de-Tabelas-em-Transfer%C3%AAncia-entre-Empresas-Filiais?source=search)
* **Transferências entre Centro de Custo:** O sistema efetua a troca do centro de custo do funcionário.
* **Transferências entre Matrículas:** Este tipo de transferência é permitida apenas no mês de admissão do funcionário, e enquanto não houver movimentação acumulada. Além disso, será permitido apenas quando não foi efetuado outro tipo de transferência ou movimentação do funcionário.
* **Transferência entre Departamentos:** O sistema efetua a troca do departamento do funcionário.
* **Transferência de Processo do funcionário:** O sistema efetua a troca do processo de folha do funcionário. Este tipo de transferência só é permitida quando os processos estão abertos no mesmo período, por exemplo, o funcionário está no processo 0001 onde o roteiro período está aberto em 05/2025, então a transferência só poderá ser feita se o novo processo estiver aberto em 05/2025 também.
* **Transferência Externa:** O sistema realiza o desligamento do funcionário afim de informar que este foi transferido para uma outra empresa que não está no mesmo ambiente Protheus
* **Transferência de posto:** Quando a hierarquia por controle de posto é utlizada, o Departamento fica vinculado ao Posto. Assim, ao realizar a transferência, o Protheus habilita o campo Posto, que já está associado ao Departamento. Dessa forma, ao selecionar o Posto, o Departamento é preenchido automaticamente.  
  OBS: Abaixo detalhes para configuração do posto :  
  [Configuração do campo RA\_POSTO](https://tdn.totvs.com/pages/releaseview.action?pageId=567758039)  
  [RH - Linha Protheus - ORG - Como cadastrar um Posto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36422863978775-RH-Linha-Protheus-ORG-Como-cadastrar-um-Posto)

Para efetuar a transferência siga os passos abaixo:

Acesse: **Gestão de Pessoal/ Atualizações/ Funcionários/Transferências**   
Em Outras Ações, selecione a opção **Transferir**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33722332226711)

O Sistema apresenta uma janela para seleção dos funcionários que serão transferidos. Nessa tela estão disponíveis as seguintes opções para seleção dos funcionários:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33722301606935)  
  
**Pesquisar**: permite pesquisar os dados dos funcionários cadastrados.  
**Marcar/Desmarcar Todos:** permite selecionar até 50 funcionários por vez ou desmarcar todos os que já tenham sido selecionados.   
**Filtro**: permite elaborar um filtro, para apresentar somente os funcionários cujos dados atendam à solicitação do filtro.  
  
Confirmados os funcionários para a transferência, o Sistema apresenta nova janela onde a tela é dividida em duas pastas:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33722332235671)

**Dados Transferência:** Informações para transferência como Empresa, Filial, Matrícula, Centro de Custo, Departamento, Processo.  
**Dados Cadastrais:** Outros dados cadastrais dos funcionários, que podem ser configurados através da opção Config. campos, como por exemplo a função, cargo, o qual passamos um exemplo ao final do artigo.

Nas duas pastas, os campos estão dispostos em dois grupos.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33722332238871)

**Origem:** São os dados atuais do funcionário. Por isso não é possível alterá-los.  
**Destino:** Deve-se informar os novos dados que o funcionário terá após a transferência.

Após conferir os dados, clique em **Confirmar:**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33722301614359)

Ao final do processamento da Transferência, é **emitido um log** com as alterações efetuadas e um histórico da movimentação é gerado no **Arquivo de Transferência - SRE**  
No exemplo abaixo, foi efetuado apenas uma transferência de centro de custo.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33722332243991)

**Saiba Mais**  
[Manual Transferências](https://tdn.totvs.com/pages/viewpage.action?pageId=815569538)  
[RH - Linha Protheus - GPE - Com o incluir campos na rotina de transferência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057497454-RH-Linha-Protheus-GPE-Com-o-incluir-campos-na-rotina-de-transfer%C3%AAncia)  
[RH - Linha Protheus - GPE - Movimentação de Tabelas em Transferência entre Empresas/Filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057237614-RH-Linha-Protheus-GPE-Movimenta%C3%A7%C3%A3o-de-Tabelas-em-Transfer%C3%AAncia-entre-Empresas-Filiais?source=search)  
[RH - Linha Protheus - GPE - Transferência de funcionário vindo de outro Sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413843598743-RH-Linha-Protheus-GPE-Transfer%C3%AAncia-de-funcion%C3%A1rio-vindo-de-outro-Sistema)  
[RH - Linha Protheus - GPE - Transferência de funcionário por processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051970893-RH-Linha-Protheus-GPE-Transfer%C3%AAncia-de-funcion%C3%A1rio-por-processo?source=search)  
[RH - Linha Protheus - GPE - eSocial - S-2299 - Preciso fazer a Transferência de trabalhadores do Protheus para uma empresa que não utiliza o Protheus, como fazer isso no sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023167651-RH-Linha-Protheus-GPE-eSocial-S-2299-Preciso-fazer-a-Transfer%C3%AAncia-de-trabalhadores-do-Protheus-para-uma-empresa-que-n%C3%A3o-utiliza-o-Protheus-como-fazer-isso-no-sistema)
