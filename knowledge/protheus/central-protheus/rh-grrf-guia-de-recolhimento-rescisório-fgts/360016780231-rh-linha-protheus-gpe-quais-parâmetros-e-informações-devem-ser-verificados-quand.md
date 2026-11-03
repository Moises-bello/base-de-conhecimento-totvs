---
article_id: 360016780231
category: RH - GRRF (Guia de Recolhimento Rescisório - FGTS)
content_hash: dfcf4be9adc6ed1cdeda52decd185a8f1abfc3b1dc8b782651c5f0abfd1a0b47
fetched_at: '2026-06-28T22:43:32.420758+00:00'
product: protheus
section_id: 360010781714
source: central-protheus
title: RH - Linha Protheus - GPE - Quais parâmetros e informações devem ser verificados
  quando o arquivo GRRF está inválido
type: support-article
updated_at: '2021-04-30T18:18:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016780231-RH-Linha-Protheus-GPE-Quais-par%C3%A2metros-e-informa%C3%A7%C3%B5es-devem-ser-verificados-quando-o-arquivo-GRRF-est%C3%A1-inv%C3%A1lido
---

**Dúvida**Quais parâmetros e informações devem ser verificados quando o arquivo GRRF está inválido? (Erro 385)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 11  
  
**Solução**Ao tentar validar o arquivo GRRF na SEFIP o sistema apresenta o erro 385- Arquivo GRRF inválido:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012815431/mceclip0.png)

Para correção do problema acesse: SIGACFG: **CFGX032**- Ambientes/Empresas/Filial:

Altere o campo **Telefone** conforme a estrutura abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012815651/mceclip1.png)

O campo número de telefone (M0\_TEL) possui tamanho de 14 caracteres e será padronizado conforme abaixo:

- Posição 1 e 2 (caracteres 1 e 2) – Destinam-se à informação DDI;  
- Posição 3 (carácter 3) – Utilização do carácter - hífen, definindo a separação para a próxima informação;  
- Posição 4 e 5 (caracteres 4 e 5) – Destinam-se à informação DDD;  
- Posição 6 (carácter 6) – Utilização do carácter - hífen, definindo a separação para a próxima informação;  
- Posição 7 em diante (caracteres 7 a 14) – Destinam-se à informação Telefone.  
  
**Exemplo**: 55-11-20997000

**Importante:**  
Somente deverá ser utilizado o caráter hífen - como delimitador das informações DDI, DDD e Telefone.  
Não deverão ser utilizados quaisquer outros caracteres especiais, tais como abaixo:  
( ) , . ; : / ? < > @ $ # % ! & \* \_ + = [ ] { }   
  
1. Em Microsiga Protheus TOTVS SmartClient, digite SIGACFG no campo Programa Inicial.  
2. Informe a senha de **administrador** do ERP Microsiga Protheus, clique em **ok**, selecione a Empresas/Filial e confirme o acesso.  
3. Acesse a opção Empresas / Arquivos / Criação de Empresas.  
4. Selecione a Empresa / Filial, clique no Botão Editar e efetue as alterações no telefone conforme as regras acima.  
5. Após a alteração, clique em Gravar e confirme as alterações.  
6. Caso o cadastro apresente mais de uma Empresa e / ou Filial, as alterações acima deverão ser realizadas em todas, levando-se em consideração os códigos de DDD e telefone para cada uma delas.  
7. Após a alteração, clique em Sair e finalize o acesso ao módulo Configurador.  
  
**Verificar também:**

1. Verificar se o arquivo de folha de pagamento está de acordo com o Leiaute de Folha de Pagamento da GRRF Eletrônica;

2. Verificar se o conectividade esta atualizado;

3. Verificar se e a mesma matricula da rescisão;

4. Verificar se existe a informação esta no TXT;

5. Comparar as datas que estão na rescisão com a data que esta nos parâmetros da geração (**data de geração, data de homologação, data de demissão e data de recolhimento, sendo esta a mesma data de homologação**).
