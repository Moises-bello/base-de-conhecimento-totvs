---
content_hash: 1af2e4fda83e79872f6fd2caa0331652616c31f111921e7e53b0137719822ed6
fetched_at: '2026-06-29T00:10:56.055837+00:00'
page_id: '590248381'
product: rm
source: tdn-rm
title: TOTVS Assinatura Eletrônica - Documento Técnico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=590248381
version: 33
---

## **01. Apresentação**

Este documento tem por objetivo apresentar os passos necessários para disponibilizar no DataServer da linha RM a integração com o Totvs Assinatura Eletrônica.

## **02.****Configuração**

Para configurar o RM x Totvs Assinatura Eletrônica é necessário informar nos parâmetros globais o caminho das API's do Totvs Assinatura Eletrônica.

## **03.****Habilitar Meu DataServer**

Para habilitar a utilização do Totvs Assinatura Eletrônica basta informar a propriedade **"AllowTotvsSign"** com o valor "**True**" na Action equivalente ao dataServer desejado.  
Sendo assim, será disponibilizado a opção do Totvs Assinatura Eletrônica em sua funcionalidade.

c#Código exemplotrue
/// Inicialização da action de contrato de locação
///
private void InitializeComponent()
{
components = new System.ComponentModel.Container();
DataServerName = "ImbContratoLocData";
FormName = "ImbContratoLocForm";
AllowTotvsSign = true;
}
}
]]>

#### **Resultado:**

## **04. Vinculo Processos**

Após habilitar a utilização do Totvs Assinatura Eletrônica, é possível condicionar a execução de processo de acordo com o status do documento anexado a entidade principal.

**Exemplo**: 

Imagine que temos um contrato de locação de imóvel em elaboração e o usuário do sistema, enviou o "documento / contrato" para o locatário assinar via Totvs Assinatura eletrônica.   
E o usuário do RM, pode efetivar o contrato no RM antes mesmo do locatário assinar o documento.

**Demanda**:

Como devo codificar, para condicionar o sucesso do processo de "*Efetivação do Contrato*" com a assinatura do documento. Ou seja,  preciso que seja a apresentando mensagem de erro tratado para o usuário do RM caso ele tente efetivar o contrato para o documento não assinado.

**04.1 Disponibilização dos processos**

Para disponibilizar os processo para o usuário possa vincular com o documento, basta preencher a propriedade "**ProcessValidationTotvsSignActions"**

c#Código exemplo true
/// Inicialização da action de contrato de locação
///
private void InitializeComponent()
{
components = new System.ComponentModel.Container();
DataServerName = "ImbContratoLocData";
FormName = "ImbContratoLocForm";
// Libera o Totvs Assinatura eletrônica para o dataServer
AllowTotvsSign = true;
// Processo de efetivar contrato de locação
ProcessActions.Add("ImbEfetivarContLocAction", true);
//Disponibilização de processo na tela de envio de documento do Totvs Assinatura
ProcessValidationTotvsSignActions.Add(new RMSProcessTotvsSignInfo()
{
ActionName = nameof(ImbEfetivarContLocAction),
LabelProcess = Properties.Resources.SImbCaptinEfetivacaoContratoTotvsSign
});
ProcessValidationTotvsSignActions.Add(new RMSProcessTotvsSignInfo()
{
ActionName = nameof(ImbContratoLocEscalonamentoAction),
LabelProcess = Properties.Resources.SImbCaptinEfetivacaoEscalonamentoTovsSign
});
ProcessValidationTotvsSignActions.Add(new RMSProcessTotvsSignInfo()
{
ActionName = nameof(ImbEfetivarAditivoContLocBaseAction),
LabelProcess = Properties.Resources.SImbCaptinEfetivacaoAditivoTovsSign
});
ProcessValidationTotvsSignActions.Add(new RMSProcessTotvsSignInfo()
{
ActionName = nameof(ImbEncerrarContLocAction),
LabelProcess = Properties.Resources.SImbCaptinEfetivacaoEncerramentoTovsSign
});
}
]]>

#### **Resultado:**

Os processo que foram preenchidos na action na lista **ProcessValidationTotvsSignActions** são apresentando no cadastro do documento.

Observação:  
  
Caso a "action" não possua processos definidos não será exibido a página de seleção, os processos marcados para validar assinatura eletrônica serão gravados na tabela GINTEGRACAOTOTVSSIGNRESTRICAO

**04.2 Validação dos processos**

Após a exposição dos processo, os mesmo são exibidos para o usuário RM na aba de validações . Mas ainda não é suficiente, pois você tem apenas quais os processo foram marcados pelo usuário para "Validar" na tela do documento. Precisamos dessa informação em camada server para que o analista codifique sua validação.

Foi disponibilizado método na framework  cujo sua responsabilidade e retornar informações referente documento anexado ao seu "DataServer" Principal. Sendo assim, você pode consumir esse método e implementar sua validação. Você deverá adicionar em seu Facade, uma chamada para o método "RetornarDadosArquivo(actionName, serverName, pkValues)" disponível na interface IGlbTotvsSignMod. E agora e utilizar o seu metodo que criou em seu facade.

c#Código exemplotrue
///
///
/// Action que deseja localizar
/// Nome do dataserver que foi o anexo do documento: Exemplo: ImbContratoLocData
/// Pk da entidade Principal. Exemplo:1;45 Coligada =1 e CodContrato=45
/// 
public List RetornarDocumentoTotvsSign(string actionName, string serverName, List pkValues)
{
List retorno = new List();
using (var totvsSign = CreateModule("GlbTotvsSignMod"))
if (totvsSign.IsConfiguracaoIntegracaoTotvsSign())
{
totvsSign.RetornarDadosArquivo(actionName, serverName, pkValues)
?.ForEach(doc => retorno.Add(doc));
}
return retorno;
}
}
]]>
