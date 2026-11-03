---
article_id: 360025596232
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: 66b7b23cdf58c6dfc6b1a6fb37874de876e4c049317c598defcd221bf9269bc4
fetched_at: '2026-06-28T22:45:35.600053+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - UBA - Exibição de campo reservado
type: support-article
updated_at: '2025-06-18T16:42:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025596232-Agro-Linha-Protheus-UBA-Exibi%C3%A7%C3%A3o-de-campo-reservado
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21893787558679)***Tempo aproximado para leitura: **00:01:40 min****Dúvida**Na rotina de **Talhões - AGRA010** existem alguns talhões cadastrados que estão atualmente em desuso, então seria interessante uma forma para bloquear estes cadastros, a fim de que não sejam confundidos com outros cadastros utilizados frequentemente. É possível que isso seja feito?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão - Versão 12  
  
**Solução**  
**Sim**, é possível que isso seja feito por meio da configuração do campo reservado **\_MSBLQL** que é padrão do **Microsiga Protheus.**A seguir há uma explicação sobre o funcionamento deste campo, especificamente para a rotina de **Talhões** do módulo de **Agroindústria**.  
  
**1.** É necessário que, por meio do configurador, o campo **NN3\_MSBLQL** seja habilitado. Depois, é necessário salvar as alterações;

![F1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360024792492)

**2.** Acesse o ambiente utilizando o **usuário administrador do Sistema**;

![f2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360024804491)

**3.** Ao acessar o Cadastro que necessita ser alterado, o campo de **Bloqueio** será exibido na tela, então basta assinalar a opção desejada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024804711)

**Importante**  
Os demais usuários do sistema não possuem permissão para realizar alterações no campo de bloqueio, enquanto o usuário administrador poderá alterá-lo sempre que necessário.  
Os cadastros que forem bloqueados por meio deste campo, serão exibidos, tanto para o usuário administrador, quanto para os demais usuários, com cor distinta dos outros cadastros, para que sejam facilmente identificados como bloqueados.  
  
**Saiba Mais**Mais informações sobre o **Campo Reservado** podem ser consultadas no link abaixo:  
[Campo Reservado \_MSBLQD e\_MSBLQL](http://tdn.totvs.com/display/public/PROT/Campo+Reservado+_MSBLQD+e+_MSBLQL)
