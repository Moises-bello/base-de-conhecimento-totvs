---
article_id: 360044763254
category: RH - Provisão
content_hash: c562ac77e907dc3789a49760d8bda45861abd942e6849a810d3dcf468efce82c
fetched_at: '2026-06-28T22:43:56.032197+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Provisão com Salário, Dias de Férias ou Avos de
  13º Salário Zerados
type: support-article
updated_at: '2025-08-04T17:55:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044763254-RH-Linha-Protheus-GPE-Provis%C3%A3o-com-Sal%C3%A1rio-Dias-de-F%C3%A9rias-ou-Avos-de-13%C2%BA-Sal%C3%A1rio-Zerados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28920160479767) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como corrigir o Cálculo de Provisão, quando o mesmo é emitido com Salário, Dias de Férias ou Avos de 13º Salário Zerados?

**Ambiente**TOTVS RH  TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - Todas as Versões

**Solução:**Ao emitir os Relatórios ou Consultar os Cálculos de Provisão, o Salário, Dias de Férias ou Avos de 13º Salário são apresentados Zerados, como no exemplo abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061492054)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062395313)

Para solucionar essa dúvida, realize os seguintes passos:  
1. Acesse: Atualizações / Funcionário / Funcionários e Verifique se o campo Salário (RA\_SALARIO) está preenchido corretamente no Cadastro do Funcionário;  
  
2. Acesse: Atualizações / Funcionários / Controle Dias de Direito e Verifique se há Período Aquisitivo Ativo para o funcionário;  
  
3. Aplique o último Pacote RH Expedição Contínua, conforme o release da sua base.  
Para realizar o Download do Pacote clique no endereço abaixo:

12.1.2310: <https://suporte.totvs.com/portal/p/10098/download#detail/1123885>   
**RELEASE 12.1.2310 SOMENTE PARA CLIENTES COM GARANTIA ESTENDIDA**  
12.1.2410: <https://suporte.totvs.com/portal/p/10098/download#detail/1170810>   
  
Observação: Aplique-o em Base de Teste, e Realize um Backup do RPO.

4. Verifique se o parâmetro MV\_CSALINC está preenchido com data anterior à competência do cálculo da provisão. Por exemplo, caso esteja processando as provisões de Agosto/2023, altere o conteúdo do parâmetro para 202307. Em seguia, realize o Logoff no Protheus.  
  
5. Exclua o Cálculo das Provisões e Processe novamente, preenchendo o campo "Tipo de Provisão" com a opção "Ambas".  
Para mais informações sobre como Excluir o Cálculo das Provisões em lote [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411059191703-RH-Linha-Protheus-GPE-Como-Excluir-Em-Lote-o-C%C3%A1lculo-das-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio).

**Saiba Mais**  
[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)  
[Parâmetro MV\_CSALINC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11899851782423-RH-Linha-Protheus-GPE-Conceito-do-Par%C3%A2metro-MV-CSALINC)
