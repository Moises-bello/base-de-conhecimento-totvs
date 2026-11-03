---
article_id: 360033742313
category: GPE - eSocial - Periódicos
content_hash: fae7302ea8ab98cbf92bed5e38a5a1fbdd0f7829a9648982170efd40a94530b3
fetched_at: '2026-06-28T22:45:07.355840+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200/S-2299 - Para que serve a informação
  de Exposição a Agentes Nocivos e como é apurado os encargos no eSocial
type: support-article
updated_at: '2026-06-26T19:00:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033742313-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-Para-que-serve-a-informa%C3%A7%C3%A3o-de-Exposi%C3%A7%C3%A3o-a-Agentes-Nocivos-e-como-%C3%A9-apurado-os-encargos-no-eSocial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27467826757783) Tempo aproximado para leitura: 00:02:00 min****Dúvida**Para que serve a informação de **Exposição a Agentes Nocivos** e como é apurado os encargos no eSocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A informação de Exposição a Agentes Nocivos serve para informar se o Trabalhador exerce condições especiais que possam ensejar aposentadoria especial após 15, 20 ou 25 anos de trabalho sob exposição a agentes nocivos prejudiciais à sua saúde e integridade física, é devida pela empresa ou equiparado a contribuição adicional destinada ao financiamento das aposentadorias especiais.  
  
As alíquotas do adicional são incidentes sobre a remuneração paga, devida ou creditada ao segurado empregado e trabalhador avulso.  
  
Segue abaixo a relação de Exposição X Alíquota divulgada na [tabela 02](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-versao-s-1-2-nt-04-2024/tabelas.html#02) do leiaute vigente:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10212842233239)  
  
Essa informação é preenchida no campo Ocorrência (RA\_OCORREN) do cadastro do Trabalhador no SIGAGPE (Atualizações> Funcionários> Gestão de Funcionários ou Funcionários), ao passar pelo campo ele exibe uma consulta com as opções existentes de acordo com a antiga definição para SEFIP, porém agora também utilizada para o eSocial.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27467812589591)  
  
Essa informação é levada ao eSocial através dos eventos de remuneração S-1200 e S-2299. Abaixo a imagem no S-2299 do TAF (Atualizações> Eventos eSocial> Não periódicos> Desligamento):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27467826772375)  
  
Segue abaixo um exemplo de apuração dos encargos quando essa informação é enviada ao RET (Governo).  
  
No evento S-5001 podemos ver a **Base de Cálculo de Contribuição Previdenciária por Trabalhador** (SIGATAF> Atualização> Eventos eSocial> Totalizadores> Cont. Social por Trabalhador) apurada pelo eSocial no valor de R$ 11.839,29.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27467826777367)  
  
No evento S-5011 podemos ver a **Base de Cálculo de Contribuição Previdenciária da Empresa** (SIGATAF> Atualização> Eventos eSocial> Totalizadores> Cont. Social por Contribuinte) apurada pelo eSocial no valor de R$ 8.744,05 de Base de Cálculo normal e R$ 11.839,29 de Base de Cálculo com aposentadoria especial 15 anos, bem como também é possível visualizar as alíquotas de FAP e RAT ajustado.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042611754)  
  
No mesmo evento S-5011 podemos ver a os valores de Contribuição Previdenciária da Empresa apurada pelo eSocial, porém temos a seguinte divisão nessa situação:  
  
**001650 - CP PATRONAL - ADICIONAL GILRAT** no valor de R$ 1.420,71, sendo esse o valor referente a contribuição adicional devido a aposentadoria especial em 15 anos por motivo de exposição a agentes nocivos. Para chegar nesse valor é só multiplicar a Base de Cálculo da aposentadoria especial 15 anos no valor de R$ 11.839,29 pela alíquota prevista nessa situação de 12%, ou seja, R$ 11.839,29 X 12% = R$ 1.4720,71.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043451553)  
  
**001709 - CP PATRONAL - GILRAT AJUSTADO** no valor de R$ 617,50, sendo esse o valor referente ao SAT (Seguro Acidente do Trabalho). Para chegar nesse valor é só somar toda a base de Contribuição Previdenciária da Empresa no valor de R$ 20. 583,34 (R$ 11.839,29 + R$ 8.744,05) e multiplicar pela alíquota de RAT Ajustado de 3%, ou seja, R$ 20. 583,34 X 3% = R$ 617,50.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043451613)  
  
Este é um cenário exemplificativo com valores fictícios com intuito de auxiliar na conferência da apuração de Contribuição Previdenciária Patronal e entender como o RET (Governo) processa determinadas informações enviadas para a base do eSocial.

**Saiba mais:**Para adquirir mais conhecimento acesse os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://informa.totvs.com/)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Para conhecimento dos eventos futuros, acessa a nossa página ***[TOTVS Informa](https://informa.totvs.com/)*** selecione em categorias a área e pesquise por "**Eventos**".
