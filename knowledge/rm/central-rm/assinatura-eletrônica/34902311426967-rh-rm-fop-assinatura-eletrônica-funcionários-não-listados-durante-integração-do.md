---
article_id: 34902311426967
category: Assinatura Eletrônica
content_hash: b9b0c6534033de3c9a5b37c4e639bd284cc7432c52f0999caf3efdcf47d85201
fetched_at: '2026-06-28T22:46:44.058123+00:00'
product: rm
section_id: 4403549405207
source: central-rm
title: 'RH - RM - FOP - Assinatura Eletrônica: Funcionários não listados durante integração
  do aviso/recibo de férias'
type: support-article
updated_at: '2025-12-02T17:10:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34902311426967-RH-RM-FOP-Assinatura-Eletr%C3%B4nica-Funcion%C3%A1rios-n%C3%A3o-listados-durante-integra%C3%A7%C3%A3o-do-aviso-recibo-de-f%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34902311386647) Tempo aproximado para leitura: 00:03:30 min**

**Dúvida**  
Ao tentar enviar o aviso ou o recibo de férias para o colaborador  através da integração com o TOTVS Assinatura Eletrônica, nenhum funcionário é listado; Como exibir os funcionários para disparo do documento?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
A rotina de disparo do relatório de Recibo de Férias somente conseguirá encontrar o funcionário caso as férias estejam no status Marcadas ou Pagas e com o recibo calculado. Para o aviso de férias, basta que as férias do funcionário já estejam marcadas - ou seja, aprovadas pelo Gestor e pelo Departamento Pessoal.

Caso as condições sejam diferentes das citadas acima, não serão exibidos resultados no momento de selecionar os colaboradores.

Além disso, deve ser observado nas configurações do relatório que será integrado (Dentro do módulo de Folha de Pagamento, aba Assinatura Eletrônica, opção Tipos de Relatórios, edite o tipo de relatório), verifique como está definida as “Opções de envio de aviso de férias”. Marque a opção “Não validar essa regra” -  dessa forma, não serão validadas datas utilizando umas das regras anteriores e, para a geração **será necessário incluir a data conforme o tipo do relatório**, na primeira tela do processo de integração de relatórios.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36725369605527)

Ainda dentro das configurações do relatório, acesse a aba Relatórios. Valide se existe um relatório vinculado para que seja enviado e se este relatório está marcado como Ativo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36725340178583)

Caso não possua estrutura de relatório de aviso/recibo de férias padrão do book do produto no seu ambiente, o download das mesmas pode ser realizado através do TOTVS Compartilhamento. Maiores documentações da funcionalidade são encontradas na documentação abaixo:

[Framework - Linha RM - Frame - TOTVS Compartilhamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8876331402775-Framework-Linha-RM-Frame-TOTVS-Compartilhamento)

O relatório de aviso de férias padrão do sistema para base de dados SQL é o FOPREL00030 - Aviso de Férias. Caso utilize base de dados Oracle, o código do relatório padrão do sistema FOPREL00180 - Aviso de Férias (Oracle).

Com as parametrizações realizadas, salve as alterações realizadas e acesse a rotina de Processo de Integração de Relatórios. Preencha a quebra de seção como “Quebra por CNPJ (por Coligada)”.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902311387927)

Na seleção de funcionários, remova todos os filtros e marque todas as caixas de seleção antes de selecionar um funcionário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902335147799)

Selecione o grupo de relatório referente ao envio que será realizado, marque a caixa de seleção Enviar sob demanda, e preencha nos campos de Data Inicial e Data final um intervalo de tempo que corresponde ao período de férias do funcionário desejado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902311392023)

**Saiba mais:**

[RH - RM - FOP - Situação das Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5327121857175-RH-RM-FOP-Situa%C3%A7%C3%A3o-das-F%C3%A9rias)  
[RH - RM - FOP - TOTVS Assinatura Eletrônica: Como integrar relatórios de Recibo de Férias?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17710383461399-RH-RM-FOP-TOTVS-Assinatura-Eletr%C3%B4nica-Como-integrar-relat%C3%B3rios-de-Recibo-de-F%C3%A9rias)
