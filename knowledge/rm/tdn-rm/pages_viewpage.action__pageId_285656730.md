---
content_hash: ed8e103aaf7ec38e3a23e88e187c8515b7f3f3dbeace0a5840dbf01639a1941f
fetched_at: '2026-06-29T00:08:38.477834+00:00'
page_id: '285656730'
product: rm
source: tdn-rm
title: 806804 MATESTCNTFTOF01-244 DT - Sucatear o Objeto de Manutenção ao Baixá-lo
  Totalmente no TOTVS Gestão Patrimonial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285656730
version: 144
---

# Sucatear o Objeto de Manutenção ao Baixá-lo Totalmente no TOTVS Gestão Patrimonial

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo(s):** | *TOTVS Gestão Patrimonial e TOTVS Manutenção.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Baixas.* | *PatOcorrenciaBaixasProcAction.* |  | **Rotina(s) envolvida(s)** | **Nome Técnico** | | --- | --- | | *Sucateamento de Objeto.* | **MntSucatearObjetoAction.** | | *Motivo de Sucateamento.* | **MntMotivoSucateamentoAction.** | | *Cancelar Sucateamento.* | *MntCancelarSucateamentoObjetoManutencaoAction.* | |
| **Cadastros Iniciais:** | *Cadastro de Patrimônio;*  *Cadastro de Objeto de Manutenção.* |
| **Parâmetro(s):** | *Tipo de Movimento de Retirada do Estoque;*  **Baixa Total;**  ***Código do Motivo de Sucateamento.*** |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Tickets relacionados** | 806804. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *[MATESTCNTFTOF01-244](http://jiraproducao.totvs.com.br/browse/MATESTCNTFTOF01-244)* |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *SQL e Oracle.* |
| **Tabelas Utilizadas:** | *OFMOTIVOSUCATEAMENTO.* |
| **Sistema(s) Operacional(is):** | *Windows.* |

## Descrição

Implementado na rotina de Baixa de Patrimônio no TOTVS Gestão Patrimonial o Sucateamento do Objeto, caso o Bem esteja integrado com o Objeto de Manutenção e esta seja uma Baixa Total.

Sendo assim, ao completar o processo de Baixa Total o Objeto de Manutenção será Sucateado, impedindo o usuário de abrir qualquer tipo de OS (Ordem de Serviço) para o mesmo.

O Objeto de Manutenção somente será sucateado se atender as premissas que seguem:

* Não possuir OS(s) em andamento;
* Não for um objeto agregado;
* Não ter sido transferido;
* Existir alguma ordem de serviço em andamento para o objeto, seu(s) ancestral(is) ou descendente(s).

Caso alguma das consistências acima sejam apresentadas, o Bem não será baixado e o Objeto não será sucateado.

Em relação aos registros integrados que já se encontram na base de dados o comportamento do sistema será de acordo com a tabela abaixo:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **TOTVS Gestão Patrimonial x TOTVS Manutenção** | | | | | |
| **Bem-Patrimonial** | **Objeto de Manutenção** | **Pode Baixar** | **Pode Sucatear** | **Pode Cancelar** | **Comportamento do BackOffice** |
| Não se aplica. | IdObjOF. | Não se aplica. | Sim. | Sim. | Continuará sendo possível sucatear e cancelar o sucateamento do objeto pelo TOTVS Manutenção. |
| CodBem. | Não se aplica. | Sim. | Não se aplica. | Não se aplica. | A baixa do Bem-Patrimonial será executada normalmente sem nenhum tipo de consistência. |
| CodBem. | IdObjOF. | Sim. | Sim. | Sim. | Quando integrados, o sucateamento e o cancelamento será feito exclusivamente pelo TOTVS Gestão Patrimonial. O cancelamento de sucateamento do objeto será realizado mediante a exclusão da(s) ocorrência(s) da(s) baixa(s). |
| CodBem. **não** está Baixado Totalmente ou Baixado Totalmente em Período Anterior. | IdObjOF está Sucateado. | Sim. | Não se aplica. | Sim. | A baixa do Bem-Patrimonial será executada normalmente sem nenhum tipo de consistência.  Pelo TOTVS Manutenção será possível cancelar o sucateamento, se o Bem-Patrimonial não foi baixado totalmente. |
| CodBem. **está** Baixado Totalmente ou Baixado Totalmente em Período Anterior. | IdObjOF. | Não se aplica. | Sim. | Sim. | No TOTVS Manutenção será possível sucatear o objeto, uma vez que o bem-patrimonial já foi baixado totalmente.  O cancelamento de sucateamento do objeto será realizado mediante a exclusão da(s) ocorrência(s) da(s) baixa(s) no TOTVS Gestão Patrimonial. |

**Legenda:**

* **IdObjOF** = Objeto de Manutenção.
* **CodBem** = Bem-Patrimonial.

Esta alteração se fez necessária pois pode ocorrer da Empresa vender um Bem da sua frota, por exemplo, e como essa integração não existia, ocorria de usuários realizarem aberturas de OS e Solicitações de Peças e Serviços para Objetos de Manutenção que não pertenciam mais a Empresa.

**Observação: Na Baixa Parcial o Sucateamento do Objeto não será executado, somente na Baixa Total.**

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações do patch 12.1.16.156 e a execução do script [SCRIPT\_INTEGRADOPATRIMONIO.zip] para a criação do novo campo inserido na base de dados.

Para executar o Script é necessário seguir os passos descritos no documento abaixo:

 - <http://tdn.totvs.com/display/public/rm/Executor+de+Scripts+RM>

**Para a Release 12.1.18 (e posteriores) não é necessário executar o Script na Base de Dados.**

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No ****RM Officina**,** acesse****Opções | Parâmetros | Sistema | Identificação**.** Marque o parâmetro **Integração com o RM Bonum**:
2. Caso o Objeto de Manutenção integrado com o Bem-Patrimonial a ser baixado esteja **Em Estoque** é necessário retirar o mesmo do estoque para que a Baixa seja realizada e o Objeto possa ser Sucateado. Para isso, acesse **Processos | Retirar objeto do estoque**.  
     
     
     
   Se o Objeto de Manutenção estiver **Em Estoque**, ao realizar a Baixa Total do Bem-Patrimonial integrado, a mensagem abaixo será apresentada:  
     
     
     
   A mensagem em questão é apresentada pois ao realizar a Baixa Total, o TOTVS Gestão Patrimonial irá verificar se é possível criar ocorrências para o Objeto integrado. Neste caso a integração irá verificar se é permitido realizar a transferência do objeto integrado ao bem, como o mesmo está **Em Estoque**, a ocorrência não é permitida.

## Procedimento para Utilização

1. Acessar o TOTVS Gestão Patrimonial | Cadastros | Patrimônio | Filtrar o Bem-Patrimonial integrado ao TOTVS Manutenção.
2. Selecionar o registro em questão | Processos | Baixas | Preencher os Parâmetros da Baixa de acordo com o seu processo de Negócio | Execute a Baixa do Bem-Patrimonial.  
     
     
     
   Caso nenhuma inconsistência seja apresentada e o processo for executado com sucesso o Objeto de Manutenção será sucateado.
3. Acesse o TOTVS Manutenção | Objeto de Manutenção | Objeto de Manutenção | Filtre o Objeto de Manutenção associado ao Bem-Patrimonial Baixado.  
     
     
     
   Poderá verificar que o Objeto de Manutenção em questão foi Sucateado e a partir desse momento, não será possível abrir OS para o mesmo.

## Motivo de Sucateamento

Na integração TOTVS Gestão Patrimonial x TOTVS Manutenção o Motivo de Sucateamento utilizado para sucatear o Objeto de Manutenção será o Default criado especificamente para esta integração.

Foi criado um campo na base de dados, na tabela **OFMOTIVOSUCATEAMENTO**, coluna **INTEGRADOPATRIMONIO**, para validar se o Motivo de Sucateamento está integrado com o TOTVS Gestão Patrimonial. **Este é um campo interno e o mesmo não deverá ser alterado**.

Ao executar o Script enviado pela equipe de Suporte (**estando na versão 12.1.16.156 ou superior**) ou realizado a **conversão da sua base de dados para a versão 12.1.18** o registro abaixo será criado no Cadastro de Motivo de Sucateamento.

1. Acesse o TOTVS Manutenção | Objeto de Manutenção | Tabelas de Objetos | Motivo Sucateamento | Localize o registro abaixo:  
     
     
     
   **Observação: O código do motivo de Sucateamento poderá variar de acordo com a base de dados onde o Script foi executado.**  
   O Motivo de Sucateamento default criado para ser utilizado na integração não poderá ser alterado e tampouco excluído.

## Cancelar Sucateamento do Objeto de Manutenção Integrado ao TOTVS Gestão Patrimonial

        Caso deseje cancelar o sucateamento do Objeto de Manutenção será necessário executar o processo de Exclusão de Ocorrência(s) da(s) Baixa(s) do Bem no TOTVS Gestão Patrimonial.

1. Acesse o TOTVS Gestão Patrimonial | Cadastros | Patrimônio | Filtrar o Bem-Patrimonial integrado ao TOTVS Manutenção.
2. Edite o registro em questão | Vá em Cálculos/Ocorrências | Ocorrências
3. Selecione a(s) ocorrência(s) | Processos | Exclusão de ocorrências e confirme a execução do processo  
     
     
     
   Ao excluir a(s) ocorrência(s) com sucesso o bem-patrimonial deixará de estar Baixado e assim o Cancelamento de Sucateamento do Objeto de Manutenção associado será executado.
4. Acesse o TOTVS Manutenção | Objeto de Manutenção | Objeto de Manutenção | Filtre o Objeto de Manutenção associado ao Bem-Patrimonial.  
     
     
     
   Poderá verificar que o Objeto de Manutenção teve o seu Sucateamento cancelado e o seu Estado de Conservação setado para Usado.

divs
