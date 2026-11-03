---
article_id: 360022136291
category: Ativo Fixo - Transferência
content_hash: 05793d312d77eeff1ce8bdbeb769ffdd94d765eef3bbe8aef60e0648bd4d55fc
fetched_at: '2026-06-28T22:41:52.194695+00:00'
product: protheus
section_id: 1500001536061
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA060 : Ao realizar
  transferência do ativo apresenta mensagem Help :AF060VLD'
type: support-article
updated_at: '2023-11-30T20:05:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022136291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA060-Ao-realizar-transfer%C3%AAncia-do-ativo-apresenta-mensagem-Help-AF060VLD
---

**Dúvida**

 Ao tentar realizar a transferência do ativo sistema apresenta mensagem abaixo

Help :AF060VLD

Problema: Bem não disponível para transferência ou não localizado no cadastro de ativos.Verifique o status dos ativos imobilizados cadastrados !

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019077852)

**Ambiente**  
Protheus– Ativo fixo – A partir da versão P12  
  
   
**Solução**

Verifique se o campo N1\_STATUS desses Bens que você está tentando fazer a transferência, está em 'Branco'. Por este motivo, ao realizar a transferência pode apresentar a seguinte mensagem. "AF060VLD: Bem não disponível para transferência ou não localizado no cadastro de ativos. Verifique o status dos ativos imobilizados cadastrados!"  
  
A validação esta sendo efetuada na versão 12 do Protheus, este campo não pode ficar em branco.  
  
Preenchimento do N1\_STATUS:  
0 = Pendente de Classificação  
1 = Em Uso  
2 = Bloqueado por Usuário  
3 = Bloqueado por Local  
4 = Transferência entre Filiais

 Obs : no padrão na versão P11  este campo já era preenchido na versão P12 passou a ter a validação. Diante disso sugerimos analista Inloco para ajuste do preenchimento do campo  
  
Saiba mais:  
[MP-SIGAATF - COMO FUNCIONA ROTINA ATFA060 TRANSFERÊNCIA DE ATIVO?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015091671-MP-SIGAATF-COMO-FUNCIONA-ROTINA-ATFA060-TRANSFER%C3%8ANCIA-DE-ATIVO-?source=search)

[MP - SIGAATF - N1\_STATUS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008522071-MP-SIGAATF-N1-STATUS)
