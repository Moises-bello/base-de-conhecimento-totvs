---
content_hash: 4f621d14fc7c8c15b5da9ffd9ef1d08390d25ebde2e8701f1cd78d7fecc69000
fetched_at: '2026-07-02T19:24:26.708274+00:00'
page_id: '6064411'
product: protheus
source: tdn-tec
title: ADS_ERR.DBF Como fazer para procurar dados relevantes
type: documentation
url: https://tdn.totvs.com/display/tec/ADS_ERR.DBF+Como+fazer+para+procurar+dados+relevantes
version: 3
---

BLOCK

ADS\_ERR.DBF Como fazer para procurar dados relevantes

## ADS\_ERR.DBF: Como fazer para procurar dados relevantes

O arquivo de log de erros e *warnings*, do ADS (Local ou Server), é o ads\_err.dbf.

Caso esse arquivo não seja configurado, o diretório padrão de criação desse arquivo é a raiz do *driver* onde está instalado o ADS, se utilizar ADS Server, ou o Sistema (exemplo Microsiga Protheus), se utilizar o ADS Local.

No entanto, para ter certeza que é o arquivo correto, sempre verifique a data e o horário. Essas informações devem ser as atuais, pois as mensagens sempre são gravadas nesse arquivo. Erros e *warnings* são escritos nesse arquivo e não são, necessariamente, erros críticos, mas podem ajudar a descobrir potenciais problemas no sistema. Por isso, muitas vezes é dificil de identicar um erro verdadeiro no arquivo ads\_err.dbf. Por exemplo, todas as vezes que o arquivo sigamat.emp é aberto, o arquivo sigamat.cdx por padrão também tenta abrir. Com isso, uma mensagem é gravada indicando erro 7041 (arquivo não existe). Mas esse log não gera nenhum problema para o sistema.

### Como procurar os erros no arquivo ads\_err.dbf

1. Marque o horário exato que o erro ocorreu.
2. Abra o arquivo **ads\_err.dbf** e procure o dia/horário do erro para verificar as mensagens que estão gravadas perto desse horário.  
    Uma maneira fácil de localizar, é reproduzir o erro e, em seguida, enviar o arquivo ads\_err.dbf. Desta forma, é mais fácil localizar a últimas mensagens. Mas se nada for encontrado, faça um filtro nesse arquivo para retirar esses erros, pois assim é possível verificar se algum erro relevante foi gravado.  
    Exemplo de filtro: ERROR\_CODE<>2 .AND. ERROR\_CODE<>1003 .AND. ERROR\_CODE<>7008 .AND. ERROR\_CODE<>7039 .AND. ERROR\_CODE<>7041

### Identificando e localizando os erros

Muitos códigos de erros repetidos, são gerados quando se utiliza os ambientes do ERP Microsiga Protheus.

Os erros mais comuns são:

| Código | Descrição |
| --- | --- |
| 2 | Sistema operacional não pode encontrar o aquivo. (O arquivo não existe) |
| 1003 | Erro na abertura do arquivo .NTX, .IDX ou .CDX. (O arquivo não existe) |
| 7008 | Falha na abertura do arquivo pelo servidor ADS. (O arquivo não existe) |
| 7039 | O arquivo já está aberto. |
| 7041 | Arquivo não existe. |

Para localizá-los, verifique o campo ERROR\_CODE do arquivo ads\_err.dbf.
