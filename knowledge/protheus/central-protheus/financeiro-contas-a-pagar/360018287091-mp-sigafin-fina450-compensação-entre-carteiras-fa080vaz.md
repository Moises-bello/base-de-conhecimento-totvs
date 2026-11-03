---
article_id: 360018287091
category: Financeiro - Contas a Pagar
content_hash: 6d49b785b326b5fe071b12798721f56991e57e09f98088a9bb873212345649b1
fetched_at: '2026-06-28T22:38:09.924871+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'MP - SIGAFIN - FINA450 - Compensação entre carteiras: FA080VAZ'
type: support-article
updated_at: '2021-04-28T15:19:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018287091-MP-SIGAFIN-FINA450-Compensa%C3%A7%C3%A3o-entre-carteiras-FA080VAZ
---

**Dúvida**Ao Realizar Compensação entre Carteiras o sistema exibe **HELP**: **FA080VAZ**  
   
 **Ambiente**Microsiga-Protheus – Financeiro – A partir da versão 12.1.17  
  
**Solução**Para solucionar essa mensagem, realize os seguintes passos:  
1.Acesse **Miscelânea> Arquivos> Tabela Motivo de Baixas**2.Verifique o motivo de baixa **CEC**, como está preenchido o campo **MOV.BANCARIA**.  
3.Caso o mesmo esteja como =**S**, por gentileza ajuste de acordo com o padrão do sistema e realize um novo teste.

Segue o *print* com os motivos de baixa padrão do sistema.  
![FA080VZ.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013495932/FA080VZ.png)

**Importante:** Não aconselhamos a alteração nos motivos de baixa padrões do sistema, pois possuem tratativas internas nos fontes. A alteração nos motivos de baixa padrões é passível de erros, como o apresentado nesta solicitação.**Saiba mais**  
 *<http://tdn.totvs.com/display/public/PROT/FINA0054_Tabela+de+motivos+de+baixa+-+Contas+a+Pagar+e+Receber>*
