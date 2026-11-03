---
content_hash: 568864a58c1ed73c09ddeb46fe4dcb3bb236fdfad86c2baf0bf2c098141c052e
fetched_at: '2026-06-29T00:11:10.118761+00:00'
page_id: '641459155'
product: rm
source: tdn-rm
title: Telemetria TCGI - Implementação e Funcionamento do Registro das Métricas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=641459155
version: 3
---

Este documento tem como objetivo demonstrar a forma correta para a implementação e testes do registro das métricas do produto TCGI.

**Preparando Ambiente**

1 - RM.Host.exe.config

* Acrescentar a tag <add key="tracels" value="true" />, Responsável por demonstrar no log do license se a métrica implementada está sendo registrada local e posteriormente enviada ao servidor de registros na nuvem TOTVS. Caso ainda tenha ficado duvidas, vá direto a documentação oficial:
As métricas são primeiramente registradas no host localmente com um cache local com a seguinte informação "LS006\_Local" na respectiva linha de registro local, somente é liberado para envio ao servidor de registro da métrica cerca de 10 minutos depois do registro com as informações "LS006\_Local". Então, após rodar novamente o cadastro/processo que foi criado para disparar a métrica o sistema irá buscar todos os registros de 10 minutos anterior ou com o tempo superior que estão pendentes no cache para envio com somente a identificação de "LS006\_Local" e enviar todos para o servidor de registro da métrica e a linha registrada no log do license agora terá "LS006\_......", no JSON da linha conterá todas as métricas que estavam no cache local dentro do tempo mínimo do cache.  
A Visualização dos registros oficiais no dashboard de telemetria tanto teste quanto produção, somente será possível no dia posterior aos registros no log do license terem ocorrido corretamente.

### **Implementando uma métrica:**

Exemplo - Métrica para registrar o tempo de financiamento do contrato que está sendo adicionado.

***1 - Criar um objeto para preenchimento dos dados necessários a métrica que será registrada:***

public class ImbVendaMetricaFinanciamentoImobiliarioInclusaoTempo : IImbVendaMetrica  
{  
const int \_LAPTIME = 0;  
int \_QUANTIDADE = 0;

public ImbVendaMetricaFinanciamentoImobiliarioInclusaoTempo(int QtdParcelas)  
{  
this.\_QUANTIDADE = QtdParcelas;  
}  
public bool CanExecute()  
{  
return true;  
}

public ImbVendaMetricaLicenseParams GetInfo()  
{  
return new ImbVendaMetricaLicenseParams  
{  
Id = ImbMetricaConsts.GestaoImobiliáriaRmContratosImobiliariosFinanciamentoMonths,  
Rotina = Properties.Resources.SImbRotina,  
SubRotina = Properties.Resources.SImbVendaMetricaTempoDoFinanciamento,  
Laptime = \_LAPTIME,  
Quantidade = \_QUANTIDADE,  
SlotId = RMSLicenseConstants.Slots[CodSistema.Imb]  
};  
}  
}

***2 - Alterar a classe de consts de métricas deverá ser adicionado:***

public static readonly string GestaoImobiliáriaRmContratosImobiliariosFinanciamentoMonths = "gestao-imobiliaria-rm\_contratos-imobiliarios-financiamento\_months";

***3 - Alterar a classe onde se deseja registrar a métrica:***  
- no caso que estamos tratando a classe de calculo do plano de financiamento atende aos requisitos necessários. Pois possui a quantidade de parcelas para sabermos quanto tempo será o financiamento.

//Metrica para registrar o tempo de financiamento do contrato que está sendo adicionado  
var metricTempoParcelamento = new ImbVendaMetricaFinanciamentoImobiliarioInclusaoTempo(venda.Parcelas.Count);  
ImbTelemetriaUtils.RegistraMetrica(metricTempoParcelamento);

Após chamar o objeto que irá preencher todos os dados da classe de métrica, deverá chamar o serviço da classe utils passando o objeto preenchido para que a métrica seja registrada.
