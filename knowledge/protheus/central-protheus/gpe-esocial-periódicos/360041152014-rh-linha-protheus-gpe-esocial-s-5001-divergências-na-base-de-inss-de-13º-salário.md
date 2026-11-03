---
article_id: 360041152014
category: GPE - eSocial - Periódicos
content_hash: 29fca067a3427182ac4fdefaa71783e19ec42101446bb8842d73f6ffdabbc177
fetched_at: '2026-06-28T22:45:09.884180+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-5001 - Divergências na base de INSS
  de 13º Salário para Trabalhadores que receberam 13º Salário e foram demitidos no
  mesmo mês
type: support-article
updated_at: '2025-07-21T14:33:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041152014-RH-Linha-Protheus-GPE-eSocial-S-5001-Diverg%C3%AAncias-na-base-de-INSS-de-13%C2%BA-Sal%C3%A1rio-para-Trabalhadores-que-receberam-13%C2%BA-Sal%C3%A1rio-e-foram-demitidos-no-mesmo-m%C3%AAs
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26848620767127) Tempo aproximado para leitura: **00:05:00 min** **Ocorrência**Divergências na base de INSS de 13º Salário para Trabalhadores que receberam 13º Salário e foram demitidos no mesmo mês.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Nos casos em que o Trabalhador recebe 13º Salário através do roteiro 132 e é demitido no mesmo mês pode haver a dobrar da base de cálculo de INSS de 13º Salário.  
  
A causa do erro é que no momento da demissão o Sistema gera novamente os valores de 13º Salário nos IDs de cálculo **0183** e **0247** e desconta o líquido já recebido no roteiro 132, porém os IDs de cálculo **0183** e **0247** não tem incidência de INSS e isso dobra a base de cálculo de INSS do 13º Salário no eSocial.  
  
**Solução**Para essa situação foi criado o ID de cálculo **1661** e no momento da rescisão ele será gerada com valor do somatória dos IDs de cálculo **0183** e **0247**. Dessa forma, a base de INSS de 13º que já foi declarada no evento S-1200 de 13º salário será deduzida quando efetuado a geração do evento S-2299.  
  
Se não houver a verba de ID de cálculo **0247** no cálculo da rescisão, **NÃO** haverá a geração da verba de ID de cálculo **1661**.  
  
**Importante  
1.** Quando existe o 13º enviado no S-1200 de dezembro ele é gerado através do calculo efetuado no **roteiro 132**, esse mesmo calculo não pode ser enviado novamente na rescisão, ou seja no S-2299 dentro do TAF não poderia ter a linha com final 132. Para que isso não ocorra é necessario que o sistema esteja com o ultimo [**Pacote Correções Expedição Continua RH,**](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA) e após atualizar seguir as seguintes orientações para o ajuste.

* Excluir o S-2299 do TAF e Governo;
* Gerar novamente o S-2299 no GPE conforme orientação do artigo: **[Como retificar uma rescisão através do SIGAGPE sem precisar excluir o calculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020865371)**

**2.** Verifique se as verbas de ID 0183 e 0247 estão corretas, elas não tem incidência de INSS folha e eSocial conforme documentação: **[Configuração de verbas de desconto de 13º salário na rescisão.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059185253)  
  
3.** A verba de ID 1661 é do tipo base desconto, e tem incidência apenas para o eSocial, configure conforme documento:**<https://tdn.totvs.com/x/gqLlGg>  
  
Observação**Apenas para quem não tem o ID de cálculo **1661** no cálculo da Rescisão e o período já está fechado no **SIGAGPE** será necessário realizar rodar um RDMAKE de acordo com os procedimentos descritos abaixo:  
  
**A.** Leia o boletim técnico abaixo e criei uma verba com o ID de cálculo **1661**:   
[**Rescisão Posterior A 2ª Parcela do 13º gera Base INSS 13º indevida no S-2299**](https://tdn.totvs.com/pages/releaseview.action?pageId=451256962)  
  
**B.** Compile o RDMAKE **UPDBINRES** para seu RPO, Para ter acesso ao RDMAKE **UPDBINRES** baixe o pacote de expedição continua do RH: [Pacote e Dicionário Correções Expedição Continua RH](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA)  
  
Leia o Boletim Técnico: <https://tdn.totvs.com/x/D4uMHw>  
Para a utilização da rotina **UPDBINRES**, deverá ser efetuado a inclusão manual no menu do módulo SIGAGPE, cadastrando o item como função de **usuário**.   
  
Verifique o artigo [**Compilação de RDMakes**](https://tdn.totvs.com/pages/viewpage.action?pageId=73077498) para saber como compilar um RDMAKE em seu RPO.  
  
Após rodar o RDMAKE **UPDBINRES** será gerado no cálculo da Rescisão o ID de cálculo **1661**: **![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055573113)** **Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
**[RH - Linha Protheus - GPE - eSocial - S-2299 - Como retificar uma rescisão através do SIGAGPE sem precisar excluir o calculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020865371)**  
**[RH - Linha Protheus - GPE - eSocial - Como retificar ou reprocessar os Totalizados (DCTFWEB) no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025678254)**  
[Artigos Calculo 13º Salario](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
