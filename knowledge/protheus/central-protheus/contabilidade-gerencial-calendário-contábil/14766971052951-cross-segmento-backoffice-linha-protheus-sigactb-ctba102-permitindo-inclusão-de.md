---
article_id: 14766971052951
category: Contabilidade Gerencial - Calendário Contábil
content_hash: 29f1c18b2042e173be0aba79c98984015287e4f401e55ac4aeda1b2494367f34
fetched_at: '2026-06-28T22:41:03.366340+00:00'
product: protheus
section_id: 1500001537301
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 - Permitindo
  inclusão de lançamentos mesmo com calendário bloqueado.
type: support-article
updated_at: '2026-01-15T20:48:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14766971052951-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Permitindo-inclus%C3%A3o-de-lan%C3%A7amentos-mesmo-com-calend%C3%A1rio-bloqueado
---

**Ocorrência**

Sistema Permitindo Inclusão/Alteração de lançamentos mesmo com calendário bloqueado.

**Ambiente**

Microsiga Protheus – Contábil – A partir da versão 12.1.2210  
  
**Solução:**

**Verifique se o parâmetro MV\_CTVBLOQ está configurado para validação do bloqueio.**  
Conteúdo do parâmetro:

1 - Verifica o bloqueio.

2 - Não verifica o bloqueio.

O parâmetro possui três posições de validação, respeitando a seguinte sequência: Moeda, Calendário e Câmbio.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31939679372183)**

Caso a segunda posição esteja com o valor "2", altere para "1" e verifique se o bloqueio passa a ocorrer conforme o esperado.

**Verifique se o parâmetro MV\_CTFBLOQ está configurado para validação de todos os programas:**

( **ALL** ) todos os programas que geram lançamentos contábeis (relacionados no tópico seguinte) serão considerados para validação de bloqueio de moeda, calendário e cambio.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37710186456215)

**Se o problema persistir, siga as instruções abaixo:**

**1º - Verifique o** ***status*** **do calendário e a amarração à moeda:**

* [O intervalo de datas informadas não poderá ser processado.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020540691-MP-SIGACTB-CTBA102-O-intervalo-de-datas-informadas-n%C3%A3o-poder%C3%A1-ser-processado-?source=search)
* [Como abrir período contábil bloqueado/fechado para movimentação?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006722952-MP-SIGACTB-CTBA010-Como-abrir-per%C3%ADodo-cont%C3%A1bil-bloqueado-fechado-para-movimenta%C3%A7%C3%A3o-?source=search)

Para o correto funcionamento, é necessário que as tabelas abaixo estejam devidamente populadas e com o mesmo compartilhamento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31939679373207)  
Para mais detalhes verifique:  [Compartilhamento de tabelas SIGACTB](https://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB)

**2º- Verifique se os processos da funcionalidade "Bloqueio por Processo" existem conforme descrito abaixo:**

Acesse a rotina CTBA010 Calendário Contábil:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14766712853527)

Clique na opção "outras ações" > bloqueio por processo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14766739479831)

Selecione o período e verifique se os processos existem para todos os períodos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14766788807831)

**Caso os processos não sejam criados ao acessar a rotina**, será necessário rodar o **UPDDISTR** com o último pacote acumulado do módulo contábil disponível no portal, pois trata-se de uma tabela autocontida, que é criada automaticamente.

Poderá obter o pacote através do link abaixo: [Pacotes de Atualização - Contabilidade Gerencial](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)

Após a aplicação do pacote e execução do **UPDDISTR**, repita os passos mencionados acima.

**Se os processos ainda não forem criados, realize as verificações abaixo:**

A tabela **CQD** é autocontida, sendo criada a partir da tabela **SX5 - U1**. Verifique se a mesma está disponível conforme indicado:

1° - Acesse o configurador:

![](https://totvssuporte.zendesk.com/attachments/token/L6ei2E4pfwWDOaf15PU6uQMim/?name=inline-1536443143.png)

2° - Pesquise pela tabela "U1" e clique na opção alterar:

![](https://totvssuporte.zendesk.com/attachments/token/XNQvaxTkEILa3wtMcAFTx7Xf0/?name=inline-613278257.png)

3°- Verificar se todos os itens estão sendo demonstrado, conforme o padrão abaixo:

![](https://totvssuporte.zendesk.com/attachments/token/24DAxyHjeuB8Tdr3DlZBbRDmC/?name=inline303353440.png)

A tabela CQD é criada com base na tabela genérica U1 que fica na SX5, esta tabela acima são os processos do sistema padrão.

Caso a tabela não exista será necessário atualizar os arquivos na pasta **SystemLoad** do Protheus, e reprocessar o **UPDDISTR p**ara que recrie a tabela SX5, pois a tabela U1 é criada a partir dela.

É necessário atualizar os arquivos diferenciais e completo conforme pacotes abaixo:

Segue pacotes de dicionários para atualização:  
  
**Release 12.1.2310:**

[12.1.2310 - Dicionário de dados Diferencial](https://suporte.totvs.com/portal/p/10098/download?e=1112208)

[12.1.2310 - Dicionário de dados Completo](https://suporte.totvs.com/portal/p/10098/download#detail/1112210)

**Release 12.1.2410:**

[12.1.2410 - Dicionário de dados Diferencial](https://suporte.totvs.com/portal/p/10098/download#detail/1167447)  
[12.1.2410 - Dicionário de dados Completo](https://suporte.totvs.com/portal/p/10098/download#detail/1167445)

Pedimos que verifique se a tabela está criada e com compartilhamento correto conforme SX2.

Caso a tabela não esteja criada, deve seguir os passos:

Recrie a tabela SX5  (Realizar backup antes da baixa da tabela), para recriação da U1.

Recriar a tabela CQD (Realizar backup antes de baixa da tabela).

**Obs**: Se após estes procedimentos o sistema permitir a inclusão de lançamentos em períodos que não existem calendários seguir a documentação abaixo:

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 - Permitindo inclusão de lançamentos em períodos que não possuem calendário cadastrados.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15915842753943-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Permitindo-inclus%C3%A3o-de-lan%C3%A7amentos-em-per%C3%ADodos-que-n%C3%A3o-possuem-calend%C3%A1rio-cadastrados-)

**Saiba mais :**

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 Help: CTGDTCOMP : O STATUS DESTE PERÍODO NÃO PERMITE DIGITAÇÃO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053754813-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Help-CTGDTCOMP-O-STATUS-DESTE-PER%C3%8DODO-N%C3%83O-PERMITE-DIGITA%C3%87%C3%83O)

[MV\_CTFBLOQ - Funcoes Bloqueio Moeda Cal. Cambio CTB](https://tdn.totvs.com.br/pages/releaseview.action?pageId=6068567)

[MV\_CTVBLOQ Bloqueio de validações de Moeda, Calendário Contábil e Câmbio.](https://tdn.totvs.com.br/pages/releaseview.action?pageId=536715163)
