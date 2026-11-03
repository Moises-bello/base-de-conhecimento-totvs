---
article_id: 10390207740695
category: GPE - eSocial - Periódicos
content_hash: 21b6ae3e35731e6b7e19d13971b3060d0d3ae48616b77ca06463277ff06f6bb3
fetched_at: '2026-06-28T22:45:07.698041+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Como enviar valores de estagiário
  desligado e readmitido como CLT no mesmo mês
type: support-article
updated_at: '2026-05-27T13:39:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10390207740695-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-enviar-valores-de-estagi%C3%A1rio-desligado-e-readmitido-como-CLT-no-mesmo-m%C3%AAs
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24472883987991)** Tempo aproximado para leitura: **00:05:00** min  
  
**Dúvida:**  
Como enviar valores de estagiário desligado e readmitido como CLT no mesmo mês?  
O que deve ser feito quando existe desligamento como Estagiário e no mesmo mês efetivado como CLT?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
Para **categoria 901 (estagiário)** as verbas rescisórias são enviadas no evento S-1200. Porém se no **mesmo mês o trabalhador for efetivado como CLT**, o evento S-1200 poderá não integrar as informações da folha de pagamento, integrando apenas as verbas calculadas na rescisão.  
Isso pode ocorrer se o ambiente estiver parametrizado para enviar um evento S-1200 e S-1210 para cada filial.  
Via de regra **só é permitido transmitir para o governo um evento S-1200 por competência para cada CPF**, caso o usuário tente transmitir 2 (dois) S-1200 para o mesmo CPF dentro do mesmo empregador (mesma raiz de CNPJ) o governo retorna com o erro "*106 - Descrição: Foi Localizado no sistema um evento em duplicidade com o evento a ser enviado, mesmo Tipo de Inscrição, CPF do Trabalhador, Período de Apuração*".  
No Protheus realizamos essa tratativa através do [**Mnemônico P\_ESOCMV**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039554533-RH-Linha-Protheus-GPE-eSocial-S-1200-Para-que-serve-o-Mnem%C3%B4nico-P-ESOCMV?source=search)pois temos clientes que configuram o ambiente com filiais de raiz de CNPJ diferentes, dessa forma atendemos a necessidade de cada forma de configuração de empresas.  
  
**Solução**  
Acessar a rotina GPEA300 no caminho: Atualizações > Definições de Calculo > **Mnemônicos** e verificar os seguintes mnemônicos:

**P\_ESOCMV :** Deve ficar com .T. em todas as filiais  
**P\_MULTV:** Deve ficar com .T. em todas as filiais  
  
Sempre que houver **remunerações em vínculos diferentes** para o **mesmo trabalhador** e no **mesmo período**, os pagamentos devem ser **aglutinado no evento S-1200.** Esse procedimento deve ocorrer mesmo que o CPF esteja cadastrado em Filiais diferentes (dentro da mesma raiz de CNPJ). Só deve existir 2 (dois) evento S-1200 quando o trabalhador possui vínculos em Filiais com a raiz de CNPJ diferente (8 primeiros dígitos), pois para estes caso o RET (Governo) irá considerar as remunerações em empregadores distintos.  
  
O [**Mnemônico P\_ESOCMV**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039554533-RH-Linha-Protheus-GPE-eSocial-S-1200-Para-que-serve-o-Mnem%C3%B4nico-P-ESOCMV?source=search)deve ser habilitado (.T.) para aglutinar os pagamentos dentro do mesmo evento S-1200 no eSocial.  
Dessa maneira o mesmo xml será gerado com ambos pagamentos.  
  
**Lembre de excluir os eventos enviados incorretamente e depois gerá-los novamente no GPE após alteração do mnemônico, filtrando por CPF.**  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar funcionários com múltiplos vínculos no evento S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013550551-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-funcion%C3%A1rios-com-m%C3%BAltiplos-v%C3%ADnculos-no-evento-S-1200?source=search)  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Inconsistência do RET - 106 - Descrição: Foi Localizado no sistema um evento em duplicidade com o evento a ser enviado, mesmo Tipo de Inscrição, CPF do Trabalhador, Período de Apuração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027461452-RH-Linha-Protheus-GPE-eSocial-S-1200-Inconsist%C3%AAncia-do-RET-106-Descri%C3%A7%C3%A3o-Foi-Localizado-no-sistema-um-evento-em-duplicidade-com-o-evento-a-ser-enviado-mesmo-Tipo-de-Inscri%C3%A7%C3%A3o-CPF-do-Trabalhador-Per%C3%ADodo-de-Apura%C3%A7%C3%A3o?source=search)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina:[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus)
