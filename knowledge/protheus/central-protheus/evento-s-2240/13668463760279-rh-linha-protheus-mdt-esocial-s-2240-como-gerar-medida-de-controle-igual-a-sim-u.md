---
article_id: 13668463760279
category: Evento S-2240
content_hash: d92f7b5ce9bbc0ab582e473713755673336e01b9e1714c23c1e79beea7d631ab
fetched_at: '2026-06-28T22:45:23.585090+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Como gerar Medida de Controle
  igual a SIM utilizando EPI ou EPC no evento S-2240 e PPP
type: support-article
updated_at: '2025-03-12T21:09:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13668463760279-RH-Linha-Protheus-MDT-eSocial-S-2240-Como-gerar-Medida-de-Controle-igual-a-SIM-utilizando-EPI-ou-EPC-no-evento-S-2240-e-PPP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24726512741271) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar Medida de Controle igual a SIM utilizando EPI ou EPC no evento S-2240 e PPP?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Processo para gerar a Medida de Proteção = S

**Cenário 1**: Quando existe um EPI como Medida de Proteção:

No módulo MDT, na rotina Risco (*Atualizações - PPRA - Riscos*), deve configurar os campos **"Utiliza EPC" (TN0\_EPC)=N** e **"Nec. EPI" (TN0\_NECEPI)=S**.  
  
Não precisa ter uma medida de controle no campo Controle (TJF\_MEDCON):  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13667662392215)  
  
Ainda no cadastro de Risco, deverá vincular o EPI, entre em Ouras Ações - Relacionamentos e na aba EPI informar o produto a ser entregue:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13667740093719)  
  
Deverá realizar a entrega do EPI, e as funcionalidades deve estar igual a SIM:

- Condição de Funcionamento do EPI  
- Prazo de Validade do EPI  
- Periodicidade da Troca do EPI

**Importante**: Verifique a configuração do parâmetro **MV\_NG2EPIR**, se estiver com **2= Risco**, no cadastro de Risco deverá informar as opções citadas acima:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13667880297751)  
  
Se o parâmetro **MV\_NG2EPIR** estiver com **1= Entrega EPI**, deverá validar as informações no cadastro de EPI x Fornecedores e Funcionário x EPI.  
  
**Condição de funcionamento do EPI:** Será validado a data de entrega do EPI (Funcionário x EPI) e Período Exposição do Risco (TN0). Se em qualquer período que o funcionário estiver exposto ao risco e não possuir EPI entregue ao funcionário, o campo será geração com N - NÃO.  
  
**Prazo de Validade:** Serão analisadas todas as entregas de EPI, verificando se ele foi entregue antes do prazo de validade e substituído dentro do prazo de validade também. Foi observada a periodicidade de troca definida pelos programas ambientais, comprovada mediante recibo assinado pelo usuário em época própria.  
  
**Periodicidade da Troca do EPI:** No cadastro de EPI x Fornecedor é verificado os dias de utilização e o tipo de durabilidade, se for definido como GERAL será contabilizado os dias corridos não abatendo faltas e afastamentos, e se definido como USO, será descontado as faltas e afastamentos do funcionário.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13667997079831)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13668002157079)  
  
No módulo Configurador, deverá ajustar os parâmetros **MV\_NG2KEPI=S** e **MV\_NG2CEPC=N**No módulo TAF, em *Atualizações - Eventos eSocial - Não Periódico - Cond.Amb.Trabalhador,* na aba Fator de Risco é apresentado a informação:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13668276014615)

**Cenário 2:** Quando existe uma medida de proteção vinculada:

No módulo MDT, na rotina Risco (*Atualizações - PPRA - Riscos*), o campo **"Utiliza EPC" (TN0\_EPC)=S**e deve haver uma medida de controle no campo "**Controle" (TJF\_MEDCON)** onde, a mesma deve ter o campo **"Tipo Cont." (TO4\_TIPCTR)** com o conteúdo igual a **2-Proteção Coletiva** ou **4-Medidas Administrativas**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13668102686871)  
  
Ainda no cadastro de Risco, deverá vincular o EPC, entre em Ouras Ações - Relacionamentos e na aba EPC (medida Controle) deverá relacionar o mesmo registro do campo **Controle (TJF\_MEDCON)**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13668298255383)  
  
Na rotina *Atualizações - PPRA - Medidas Controle*, define o tipo:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13668214132119)

No módulo Configurador, deverá ajustar os parâmetros **MV\_NG2KEPI=S** e **MV\_NG2CEPC=S**No módulo TAF, em *Atualizações - Eventos eSocial - Não Periódico - Cond.Amb.Trabalhador,* na aba Fator de Risco é apresentado a informação:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13668403326743)  
  
**Observação**: O ambiente precisa estar com último Acumulado MDT: [Como fazer o download do pacote de expedição continua](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773)   
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
