---
article_id: 360038369294
category: Rescisão
content_hash: 500e794d0471934a414fb0ffa0e2483d9cab43e7e14527682fcdfca8ca5c4d50
fetched_at: '2026-06-28T22:46:55.247670+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Dias de Aviso Prévio Indenizado a cada ano trabalhado
type: support-article
updated_at: '2025-01-22T19:21:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038369294-RH-RM-FOP-Dias-de-Aviso-Pr%C3%A9vio-Indenizado-a-cada-ano-trabalhado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29426896607383)Tempo aproximado para leitura:**00:01:00 min  
  
Dúvida**Como calcular os 03 dias de indenização a cada ano de trabalho no Aviso Prévio Indenizado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**A cada um ano trabalhado o funcionário tem direito a mais 03 dias na contagem do Aviso Prévio Indenizado. A Indenização da inclusão dos 03 dias a cada ano trabalhado é realizada nas rescisões que tiverem Aviso Prévio Indenizado.  
  
Para automatizar a inclusão dos 03 dias no aviso prévio indenizado, primeiramente deverá acessar:  
  
1. Acesse: **Administração de Pessoal | Sindicato | Identificação | Fórmula de número de dias de aviso prévio.****![KCS2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360051284313)**2. No campo **Fórmula de número de dias de aviso prévio**, deverá ser criado uma nova Fórmula, no conteúdo da Fórmula, poderá ser utilizado uma **fórmula de exemplo** disponibilizada pela TOTVS.  
  
**Conteúdo da Fórmula de exemplo:**

```
DECL DiasAteDem,DataProj,TCASA2;  
SETVAR(DiasAteDem,(MAX(30,MIN(90,((TCASA)*3)+30))));  
SETVAR(DataProj,(DTD+DiasAteDem));  
SETVAR(TCASA2,GDT(1,DataProj));  
MAX(30,MIN(90,((TCASA2)*3)+30));
```

**Importante**  
A fórmula de exemplo trata-se apenas de uma sugestão, caso o Cliente queira um comportamento diferente na Fórmula, deverá ser criada/alterada pelo próprio Cliente.  
  
3. Deverá acessar o cadastro da rescisão e após preencher todos os dados, clicar no ícone **salvar** a rescisão e, em seguida, executar a fórmula através do botão **Executa Formula de Aviso Sindicato.** Nesse momento será acrescido os dias no campo **Aviso Prévio Indenizado**.  
  
**Importante**Caso for executado a fórmula antes de salvar o cadastro da rescisão, a fórmula não surgirá efeito. O processo descrito no item 3 é necessário, pois a fórmula busca a data de demissão do funcionário que somente é gravada no banco de dados após a rescisão ser salva.   
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360051615373)
