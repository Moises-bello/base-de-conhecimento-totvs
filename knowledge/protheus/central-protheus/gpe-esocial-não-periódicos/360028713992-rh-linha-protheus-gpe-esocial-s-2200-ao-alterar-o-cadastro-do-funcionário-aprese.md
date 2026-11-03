---
article_id: 360028713992
category: GPE - eSocial - Não Periódicos
content_hash: fa45096ac927376036a271948ec51878a4f7598225c03b1c2da7b414783fe42b
fetched_at: '2026-06-28T22:45:04.446853+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-2200 - Ao alterar o cadastro do funcionário
  apresenta o erro: Funcionário não enviado ao TAF. Erro: 000025'
type: support-article
updated_at: '2026-06-16T11:26:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028713992-RH-Linha-Protheus-GPE-eSocial-S-2200-Ao-alterar-o-cadastro-do-funcion%C3%A1rio-apresenta-o-erro-Funcion%C3%A1rio-n%C3%A3o-enviado-ao-TAF-Erro-000025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18021731772311) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
No módulo Gestão de Pessoal, ao tentar realizar a alteração da data de admissão ou outro campo para o eSocial, apresenta o erro: Funcionário não enviado ao **TAF**, Erro: 000025  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois existe algum evento **S-2205** ou **S-2206** pendente de transmissão para o governo.  
  
**Solução**  
1. Verificar no módulo **TAF** se existe eventos **S-2205** ou **S-2206** pendente de transmissão para o governo ou evento com inconsistência;  
1.1. Verificar através do **Histórico de Alterações** na rotina **Cadastro Trabalhador** se todos os eventos estão com Status de Transmissão = **4 - Transmitido Válido**  
Caminho: SIGATAF > Atualizações > Eventos eSocial > Trabalhador > Cadastro Trabalhador:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18021583313943)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18021589885719)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18021612286359)  
  
1.2. Verificar através da rotina **eSocial do Futuro** se existe algum S-2205 ou S-2206 pendente de transmissão ou com inconsistência.  
Caminho: SIGATAF > Miscelânia > eSocial > eSocial do Futuro:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18024450924439)  
![Exibindo smartclient_TNaUvQ7oNk.gif](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fgif&attachment_token=AOo0EEUry%2BOMk3tgoq%2FIRBXRVbgnN%2FasgYLwLp1R49U%2BIm6Y%2FDF6IP5prEDApaAiDrbwk7STGDV6PNEV2dExMwPBs1F7VBEYvVEv2RqkDoNnaL43MHsHtYwCNiqb62kG4VDC4eI3jS2DZhH63BBBxYw8cuKoOvNnAfr1uD0H3yZTMyT%2BienSR%2FNuFsEgJVsZ6DvLfnWg0tw2TMGTWtLubAMdQ0asumVHoZNpCDQvapDbHZhWsxCorfFARKHcXdtkRxKd0o8oa00UnJDMpNETlYmavyN2GDHoQvXv2sx81nNQtEzNJ25ujTavcxwlVi0sYDlyJqktna9UxovxyUeSehmxzREX%2BDFv7Thu%2FX%2F69UUF1co%2Bw9tyQg4rBlLPCPTWEuqPbsd3EnSHRJaSix84hQ9jvNC8cT68y9jACQW9oIXNNR%2FGEt72Mg7TjfgZavFUC3OjVlDF%2FU%2BQ71m83uCwFYJCgwslYqXzIobyxrH0pLkHal6ZvOf7YfvWjlyaUg2bgBQ6C9%2FnClZwrvE06a54K8YjxCC6vc6UPwARmnuKrJO8EYXcXU5BhlV3%2BzO2DZKyabCfDAG5iL62ODEcUWc%2FSI645CU%3D&sz=w1920-h955)  
  
2. Caso exista evento pendente de transmissão ou com inconsistência, realize o envio para o governo e verifique se foi protocolado.  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[Artigos S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052505613)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
